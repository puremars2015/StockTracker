# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:39:53 2022

@author: purem
"""




import yfinance as yf

stock = yf.Ticker(f"2330.TW")
df = stock.history(period="1mo",interval="1d")
print(df)



df['Date'] = df.index

rowfor2 = df.loc[:,["Date","Close"]]

r = rowfor2.to_json(orient = 'records')
print(r)