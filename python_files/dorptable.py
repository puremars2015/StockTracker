# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 00:20:43 2022

@author: purem
"""

import sqlite3

conn = sqlite3.connect('tradingview.db')
print ("--open database success--")
c = conn.cursor()
cursor = c.execute('''DROP TABLE ALERTMESSAGE''')


conn.commit()
conn.close()