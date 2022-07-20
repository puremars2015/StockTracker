import backtrader as bt

class BuyAndHold(bt.Strategy):
  def next(self):
    if self.position.size == 0:
      size = int(self.broker.getcash() / self.data)

      print(f'=== 購買 {size} 股 > 價格 {self.data.close[0]} ===')
      
      self.buy(size=size)