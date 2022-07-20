from datetime import datetime
import backtrader as bt

from strategies.SIP import SIP #引入SIP策略

cerebro=bt.Cerebro()
cerebro.addstrategy(SIP)
cerebro.broker.setcash(1000)
cerebro.broker.setcommission(commission=0.001)

data = bt.feeds.YahooFinanceData(
   dataname='./virtualdrive/TSLA.csv',
    
    # 資料起始日
    fromdate=datetime(2022, 5, 1),
    
    # 資料結束日
    todate=datetime(2022, 5, 18)
)
cerebro.adddata(data)

print('投資 > 起始資產 %.2f 💲' % cerebro.broker.getvalue())#一開始投入的資產
cerebro.run()
print('投資 > 結束資產 %.2f 💲' % cerebro.broker.getvalue())#運作後剩餘的資產

import backtrader_plotting
import matplotlib
matplotlib.use('QT5Agg')

# Your running code

cerebro.plot()