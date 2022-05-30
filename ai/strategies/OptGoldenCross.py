import math
import backtrader as bt

class OptGoldenCross(bt.Strategy):
  params = (
    ('fast', 50), ('slow', 200),
    ('order_percentage', 0.95),
  )

  def log(self, txt, dt=None):
    ''' 優化 - 黃金交叉策略 '''
    dt = dt or self.datas[0].datetime.date(0)#如果有date就用date，沒有就用最新的
    print(f'{dt.isoformat()} > {txt}')

  def __init__(self):
    self.dataclose = self.datas[0].close
    self.profit = 0#通過這一輪跑出來的總利潤是多少就放在這個變數中

    self.fast_moving_average = bt.indicators.SMA(
      self.data.close, period=self.params.fast, plotname='50 日均線'
    )

    self.slow_moving_average = bt.indicators.SMA(
      self.data.close, period=self.params.slow, plotname='200 日均線'
    )

    self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

  def next(self):
    # self.log(f'Close, {self.dataclose[0]}')

    if self.position.size == 0:
      if self.crossover > 0:
        amount_to_invest = (self.params.order_percentage * self.broker.cash)
        self.size = math.floor(amount_to_invest / self.data.close)

        self.buy(size=self.size)
      
    if self.position.size > 0:
      if self.crossover < 0:
        self.sell()
  #每一次策略跑完後就去記錄身上總獲利是多少？
  def stop(self):
    self.profit = round(self.broker.getvalue(), 2)#round只留小數位數後兩位，
    #self.broker.getvalue()可以看到自己身上的現金
    self.log(f'黃金交叉 Fast {self.params.fast} Slow {self.params.slow} 最終獲利 {self.broker.getvalue()}')