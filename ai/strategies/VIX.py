import backtrader as bt
import datetime

class VIX(bt.Strategy):
  def __init__(self):
    self.vix = self.datas[0].vixclose #最新的vix close收盤價，這是一個數列
    self.spyopen = self.datas[0].open #最新的標普500
    self.spyclose = self.datas[0].close

  def log(self, txt, dt=None):
    ''' VIX 指標 '''
    dt = dt or self.datas[0].datetime.date(0)#如果有date就用date，沒有就用最新的
    print(f'{dt.isoformat()} > {txt}')

  def next(self):
    if self.vix[0] > 35:#超過35
      self.log(f'前一個 VIX {self.vix[0]}')
      self.log(f'開盤價 {self.spyopen[0]}')

      if not self.position or self.broker.getcash() > 5000:#身上剛好沒有倉位或現金大於5000就會買進
        size = int(self.broker.getcash() / self.spyopen[0])#把現金轉換看看可以買幾股？
        print(f'買進 {size} 股 > 價格 {self.spyopen[0]}')
        self.buy(size=size)

    if len(self.spyopen) % 20 == 0:#20天為一個週期，就做多投的動作
           self.log(f"多投 5000 現金，並且不賣出. 擁有現金 {self.broker.getcash()}")
           self.broker.add_cash(5000)
    # if self.vix[0] < 12 and self.position:#self.position這種寫法代表你的變數是正的
    #   self.close()