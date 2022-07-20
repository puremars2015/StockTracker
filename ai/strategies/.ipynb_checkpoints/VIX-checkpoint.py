import backtrader as bt
import datetime

class VIX(bt.Strategy):
  def __init__(self):
    self.vix = self.datas[0].vixclose
    self.spyopen = self.datas[0].open
    self.spyclose = self.datas[0].close

  def log(self, txt, dt=None):
    ''' VIX 指標 '''
    dt = dt or self.datas[0].datetime.date(0)
    print(f'{dt.isoformat()}, {txt}')

  def next(self):
    if self.vix[0] > 35:
      self.log(f'前一個 VIX： {self.vix[0]}')
      self.log(f'SPY 開盤： {self.spyopen[0]}')

      if not self.position or self.broker.getcash() > 5000:
        size = int(self.broker.getcash() / self.spyopen[0])
        print(f'買進 {size} / SPY 價格 {self.spyopen[0]}')
        self.buy(size=size)

    if len(self.spyopen) % 20 == 0:
           self.log("多投 5000 現金，並且不賣出. 擁有現金 {}".format(self.broker.getcash()))
           self.broker.add_cash(5000)
    # if self.vix[0] < 12 and self.position:
    #   self.close()