# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 01:09:52 2022

@author: purem


https://sparkbyexamples.com/pandas/pandas-set-index-to-column-in-dataframe/
df取index跟data的方法

https://github.com/ranaroussi/yfinance

#    period=日期範圍 (1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max)
#    interval=頻率 (1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo)
"""

import requests,json
from datetime import datetime,timedelta
import yfinance as yf
import time
import pandas as pd

class MyRequest:
    
    def __GetWeekDate(self,dayObj):
        weekday = dayObj.weekday()
        
        dayDate = None
        
        if weekday != 0:
            dayDate = dayObj + timedelta(days=-weekday)
            return dayDate
            
        return dayObj
    
    def __GetMonthDate(self,dayObj):
        weekday = dayObj.weekday()
        
        dayDate = None
        
        if weekday > 4:
            dayDate = dayObj + timedelta(days=-(weekday-4))
            return dayDate
            
        return dayObj
    
    def __init__(self,date,stockCode):
        self.date = date
        self.stockCode = stockCode
 
    def GetSample(self):     
        url = "https://api.github.com/events"  
        r = requests.get(url)
        print(url)
        obj = json.loads(r.text)
        return obj       
 
    # 從證交所取得資料
    def GetStockInfo(self):     
        url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={self.date}&stockNo={self.stockCode}&_={int(datetime.now().timestamp())}"  
        r = requests.get(url)
        # print(url)
        res = json.loads(r.text)
        result = []
        for r in res['data']:
            strt = r[0].split('/')
            h = int(strt[0])+1911
            ds = f"{h}{strt[1]}{strt[2]}"
            result.append({"Date":ds,"Close":float(r[6])})
        return result
    
    # 從yfinanace取得資料
    def GetStockInfoV2(self):
        stock = yf.Ticker(f"{self.stockCode}.TW")
        df = stock.history(period=self.date,interval="1d")
        df['Date'] = df.index.map(lambda x:x.strftime('%Y%m%d'))     
        collect = df.loc[:,["Date","Close"]]
        js = collect.to_json(orient = 'records')
        result = json.loads(js)
        return result

    def GetThreeBig(self): 
        dayObj = datetime.strptime(self.date, '%Y%m%d')       
        weekDate = int(self.__GetWeekDate(dayObj).strftime('%Y%m%d'))
        monthDate = int(self.__GetMonthDate(dayObj).strftime('%Y%m%d'))
        url = f"https://www.twse.com.tw/fund/BFI82U?response=json&dayDate={self.date}&weekDate={weekDate}&monthDate={monthDate}&type=day&_={int(datetime.now().timestamp())}"  
        r = requests.get(url)
        print(url)
        obj = json.loads(r.text)
        return obj
    
    

        
    

# req = MyRequest('20220325','2330')

# res = req.GetStockInfo()

# print(res)

# print('--------------------------')

# res = req.GetStockInfoV2()

# print(res)
