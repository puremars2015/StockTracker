# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:10:09 2022

@author: Sean 馬恩奇
"""


import sqlite3
import os
import json
import pandas as pd
from datetime import datetime,timedelta




class DbHelper:
    
    def __init__(self, dbFilePath, dbTableName):
        self.dbFilePath = dbFilePath
        self.dbTableName = dbTableName

    def Destroy(self):
        print("--Destroying DB File--")
        os.remove(self.dbFilePath)
        print("--Destroying Complete--")


    def CreateAlertMessage(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Creating--")        
        c = conn.cursor()
        c.execute(f'CREATE TABLE {self.dbTableName} (ID number,MESSAGE text,SYMBOL text,EXECUTETIME text)')
        
        conn.commit()
        c.close()
      
        conn.close()
        print("--Creating Complete--") 
        
    def CreateThreeBig(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Creating--")        
        c = conn.cursor()
        c.execute(f'CREATE TABLE {self.dbTableName} (ID number,UNIT text,BUY text,SELL text,DIFF text,DATE text,EXECUTETIME text)')
        
        conn.commit()
        c.close()
      
        conn.close()
        print("--Creating Complete--") 

    def Drop(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Droping--")        
        c = conn.cursor()
        c.execute(f'DROP TABLE {self.dbTableName}')
        
        conn.commit()
        c.close()
        conn.close()
        print("--Droping Complete--") 

    def IsInit(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Checking initialize statment--")        
        c = conn.cursor()
        cursor = c.execute(f"SELECT * FROM sqlite_master WHERE type = 'table' AND name = '{self.dbTableName}'")
        row1 = cursor.fetchone()
        
        result = row1 is not None
        c.close()
        conn.close()
        print("--Checking Complete--")
        return result

    def InitAlertMessage(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Initializing--")        
        c = conn.cursor()
        c.execute(f"INSERT INTO {self.dbTableName}(ID,MESSAGE,SYMBOL,EXECUTETIME) VALUES(0,'INIT','INIT','{datetime.now()}');")
        
        conn.commit()
        c.close()
        conn.close()
        print("--Initializing Complete--")
        
    def InitThreeBig(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Initializing--")        
        c = conn.cursor()
        c.execute(f"INSERT INTO {self.dbTableName}(ID ,UNIT ,BUY ,SELL ,DIFF ,DATE ,EXECUTETIME ) VALUES(0,'INIT','INIT','INIT','INIT','INIT','{datetime.now()}');")
        
        conn.commit()
        c.close()
        conn.close()
        print("--Initializing Complete--")

    def Read(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Reading--")        
        c = conn.cursor()
        cursor = c.execute(f'SELECT * FROM {self.dbTableName} ORDER BY ID DESC')
        
        for row in cursor:
            print("ID = ", row[0])
            print("MESSAGE = ", row[1])
            print("SYMBOL = ", row[2])
            print("EXECUTETIME = ", row[3], "\n")
            
        c.close()
        conn.close()
        print("--Reading Complete--")
        
    def ReadTable(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Reading--")        
        table = pd.read_sql_query(f'SELECT * FROM {self.dbTableName} ORDER BY ID DESC',conn)
        table
        conn.close()
        print("--Reading Complete--")
        
    def ReadUs500(self):
        print(datetime.now())
        # select * from ALERTMESSAGE where SYMBOL like 'us500%' and EXECUTETIME < '2022-03-29 23:50:00.707368'
        # datetime.now() + timedelta(minutes=-5)
        conn = sqlite3.connect(self.dbFilePath)
        print("--Reading--")            
        c = conn.cursor()
        sql = f"SELECT * FROM {self.dbTableName} WHERE SYMBOL like 'us500%' and USED <> 1 and EXECUTETIME > '{datetime.now() + timedelta(minutes=-60*60)}' ORDER BY ID DESC"
        print(sql)
        cursor = c.execute(sql)
        
        result = []
        

        
        for row in cursor:
            rowResult = []
            print("ID = ", row[0])
            print("MESSAGE = ", row[1])
            if 'sell' in row[1]:
                rowResult.append('sell')
            if 'buy' in row[1]:
                rowResult.append('buy')
            print("SYMBOL = ", row[2], "\n")
            if 'h1' in row[2]:
                rowResult.append('h1')
            if 'h2' in row[2]:
                rowResult.append('h2')
            if 'm5' in row[2]:
                rowResult.append('m5')
            result.append(rowResult)
        
        print(result)
        
        # sql = f"UPDATE ALERTMESSAGE SET USED = 1 WHERE SYMBOL like 'us500%' and EXECUTETIME > '{datetime.now() + timedelta(minutes=-7)}' "
        # c.execute(sql)
         
        # conn.commit()
        
        c.close()
        conn.close()
        print("--Reading Complete--")
        
        
        for s in result:
            if s[0] == "buy" and s[1] == "h1":
                return "buy,h1"
            if s[0] == "buy" and s[1] == "h2":
                return "buy,h2"
            if s[0] == "sell" and s[1] == "h1":
                return "sell,h1"
            if s[0] == "sell" and s[1] == "h2":
                return "sell,h2"
        
        return ""
   
    def CheckSelfBusinessTradeBySelf(self,startDate,endDate):
        
        emptyDays = []
        
        empList = []
        
        
        sd = datetime.strptime(startDate, '%Y%m%d')
        ed = datetime.strptime(endDate, '%Y%m%d')
        
        sdweekday = sd.weekday()
        edweekday = ed.weekday()
        
        if sdweekday == 5 or sdweekday == 6:
            sd+=timedelta(days=+(7-sdweekday))
        
        if edweekday == 5 or edweekday == 6:
            ed+=timedelta(days=-(edweekday-4))
        
        sdstr = sd.strftime('%Y%m%d')
        edstr = ed.strftime('%Y%m%d')
 
        for i in range(int(sdstr),int(edstr)+1):
            # print(i)
            d = datetime.strptime(str(i), '%Y%m%d')
            if d.weekday() != 5 and d.weekday() != 6:
                empList.append(d.strftime('%Y%m%d'))
                
        # print(empList)
 
    
        conn = sqlite3.connect(self.dbFilePath)
        print("--Reading--")  
        c = conn.cursor()
        
        for i in empList:
            url = f"select DATE from THREE_BIG where unit = '自營商(自行買賣)' and DATE >= {i} and DATE <= {i}"
            cursor = c.execute(url)
            r = cursor.fetchall()
            if len(r) == 0:
                emptyDays.append(i)
            
        c.close()
        conn.close()
        
        print("--Reading Complete--")     
        
        return emptyDays
   
    def ReadSelfBusinessTradeBySelf(self,startDate,endDate):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Reading--")  
        c = conn.cursor()
        cursor = c.execute(f"select DISTINCT UNIT,BUY,SELL,DIFF,DATE from THREE_BIG where unit = '自營商(自行買賣)' and DATE >= {startDate} and DATE <= {endDate}")      
        collect = cursor.fetchall()
        
        c.close()
        conn.close()
        
        print("--Reading Complete--")     
        
        return collect
    
    def ReadSelfBusinessAvoidRisk(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Reading--")        
        table = pd.read_sql_query(f'SELECT * FROM {self.dbTableName} ORDER BY ID DESC',conn)
        table
        conn.close()
        print("--Reading Complete--")
    
    def ReadInvestmentTrust(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Reading--")        
        table = pd.read_sql_query(f'SELECT * FROM {self.dbTableName} ORDER BY ID DESC',conn)
        table
        conn.close()
        print("--Reading Complete--")
    
    def ReadForeignAsset(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Reading--")        
        table = pd.read_sql_query(f'SELECT * FROM {self.dbTableName} ORDER BY ID DESC',conn)
        table
        conn.close()
        print("--Reading Complete--")
    
    def ReadForeignAssetSelfBusiness(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Reading--")        
        table = pd.read_sql_query(f'SELECT * FROM {self.dbTableName} ORDER BY ID DESC',conn)
        table
        conn.close()
        print("--Reading Complete--")
    
    def ReadThreeBigTotal(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Reading--")        
        table = pd.read_sql_query(f'SELECT * FROM {self.dbTableName} ORDER BY ID DESC',conn)
        table
        conn.close()
        print("--Reading Complete--")
        
    def GetID(self):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Getting ID--")        
        c = conn.cursor()
        cursor = c.execute(f'SELECT ID FROM {self.dbTableName} ORDER BY ID DESC')
        row1 = cursor.fetchone()
        idx = row1[0]
        
        c.close()
        conn.close()
        print("--Getting ID Complete--")  
        return idx
        
    def WriteAlertMessage(self,idx,message,symbol,executetime):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Writing--")        
        c = conn.cursor()
        c.execute(f"INSERT INTO {self.dbTableName}(ID,MESSAGE,SYMBOL,EXECUTETIME) VALUES({idx},'{message}','{symbol}','{executetime}');")
         
        conn.commit()
        c.close()
        conn.close()
        print("--Writing Complete--") 
        
    def WriteThreeBig(self,idx,unit,buy,sell,diff,date,executetime):
        conn = sqlite3.connect(self.dbFilePath)
        print("--Writing--")        
        c = conn.cursor()
        c.execute(f"INSERT INTO {self.dbTableName}(ID ,UNIT ,BUY ,SELL ,DIFF ,DATE ,EXECUTETIME ) VALUES({idx},'{unit}','{buy}','{sell}','{diff}','{date}','{executetime}');")
         
        conn.commit()
        c.close()
        conn.close()
        print("--Writing Complete--") 



# db = DbHelper('tradingview.db','THREE_BIG')

# dd = db.CheckSelfBusinessTradeBySelf('20220301','20220325')



# print(dd)
