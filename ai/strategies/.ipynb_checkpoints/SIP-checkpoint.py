import backtrader as bt
from datetime import datetime
from dateutil.relativedelta import relativedelta
# relativedelta可以計算例如今天是1月1日，兩個星期後是幾月幾日？
# 策略模式作爲一種軟體設計模式，指對象有某個行爲，但是在不同的場景中，該行爲有不同的實現算法。比如每個人都要「交個# 人所得稅」，但是「在美國交個人所得稅」和「在中國交個人所得稅」就有不同的算稅方法。

#當每一次有新的資料，新的 K線進來時 self.data.datetime.date()可以讓我知道目前運行到幾月幾日
# self.data.datetime.date()>= self. _next_buy_date.date()如果遇到放假日會自動跳到下一個工作日所以要 >= 
# datetime(2010, 7, 1)從7/1日開始 relativedelta(weeks=2)指下一次是兩個禮拜後，如果months=1就是一個月後

class SIP(bt.Strategy):
    def __init__(self):
        self._next_buy_date = datetime(2010, 7, 1)#第一次購買日期
     
    
    def next(self):
        if self.data.datetime.date() >= self._next_buy_date.date():
            self._next_buy_date += relativedelta(weeks=2)

            print(f'=== {self.data.datetime.date()} 購買 1 股 價格 {self.data.close[0]} ===')
            
            self.buy(size=1)