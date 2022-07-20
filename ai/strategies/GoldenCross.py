import math
import backtrader as bt
#params = (('fast', 50), ('slow', 200), ('order_percentage', 0.95))
#參數一：快線50日，參數二：慢線200日，參數三：設定一個要讓我們保險起見，不要讓我們翻車，就是本金都賠掉，所以會設定八成
#換倉位，兩成換現金不會all in
class GoldenCross(bt.Strategy):
  params = (('fast', 50), ('slow', 200), ('order_percentage', 0.95))

  def __init__(self):
    #先訂定快線和慢線，做一個黃金交叉，crossover的指標，告訴我何時該進廠何時該出場？這個信號會是正1or負1
    #正1代表我現在快線已經壓過慢線，快線在上漲，代表市場已經上漲一段時間了，如果是慢線壓過快線，一段時間可以準備要出場
    #所以我們要計算出現在市場是正1or負1
    #bt.indicators.SMA 做快線和慢線的 self.data.close,收盤價 period=self.params.fast,區間
    #
    self.fast_moving_average = bt.indicators.SMA(
      self.data.close, period=self.params.fast, plotname=f"{self.params.fast} 日均線"
    )

    self.slow_moving_average = bt.indicators.SMA(
      self.data.close, period=self.params.slow, plotname=f"{self.params.slow} 日均線"
    )
    # self.crossover算好後會變成 正1or負1
    self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

  def next(self):
    #self.position.size == 0先判斷假設我沒有倉位(持有股的數量)，所以就需要去做進場的動作
    if self.position.size == 0:
      if self.crossover > 0:
        amount_to_invest = self.params.order_percentage * self.broker.cash
        self.size = math.floor(amount_to_invest / self.data.close)
        # math.floor()可以強制把零頭去掉的function，self.data.close當日的收盤價
        print(f'=== 購買 {self.size} 股 > 價格 {self.data.close[0]} ===')

        self.buy(size=self.size)
    #self.position.size  > 0 判斷假設我有倉位，就判斷這個市場信號是否需要離場 
    if self.position.size > 0:
      if self.crossover < 0:
        print(f'=== 賣出 {self.size} 股 > 價格 {self.data.close[0]} ===')

        self.close()