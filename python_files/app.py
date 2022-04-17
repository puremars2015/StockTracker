# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 10:11:40 2022

@author: purem
"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'


@app.route('/webhook', methods=['POST'])
def webhook():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    return "OK!"

app.run(host='220.133.234.2', port=80)