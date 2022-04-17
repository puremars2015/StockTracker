# # -*- coding: utf-8 -*-
# """
# Created on Tue Mar 22 10:50:43 2022

# @author: purem
# """

# import requests,json

# date = 20220322
# stockCode = 2345

# url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={date}&stockNo={stockCode}"

# r = requests.get(url)
# obj = json.loads(r.text)

# print(obj['data'])




# from dbhelper import DbHelper

# db = DbHelper('C:\\Users\\purem\\Desktop\\tradingview.db','ALERTMESSAGE')

# db.ReadTable()




# from datetime import datetime,timedelta,date


# d = dt.strptime('21/03/2022 01:55:19', '%d/%m/%Y %H:%M:%S')

# d = dt.strptime('21/03/2022 01:55:19', '%d/%m/%Y %H:%M:%S')


# dayObj = datetime.strptime('20220326', '%Y%m%d')

# # d = datetime.now() + timedelta(days=-5)


# d = dayObj + timedelta(days=-5)

# print(int(d.timestamp()))


# print(d.date())

# print(d.day)

# print(d.weekday())

# print(d.strftime("'%Y%m%d'"))


# for i in range(20220321,20220325+1):
#     print(i)


import requests,json

url = 'http://220.133.234.2/stockInfo'
myobj = {
    "stockCode":"2345",
    "time":"20220324"
}

x = requests.post(url, data = json.dumps(myobj) )


print(json.loads(x.text))