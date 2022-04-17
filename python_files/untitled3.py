# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 13:08:53 2022

@author: purem
"""

import sqlite3

conn = sqlite3.connect('tradingview.db')
print ("--open database success--")
c = conn.cursor()
cursor = c.execute('''SELECT * FROM ALERTMESSAGE ORDER BY ID DESC''')

for row in cursor:
   print ("ID = ", row[0])
   print ("MESSAGE = ", row[1])
   print ("SYMBOL = ", row[2])
   print ("EXECUTETIME = ", row[2], "\n")

   
conn.close()