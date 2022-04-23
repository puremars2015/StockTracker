# https://shengyu7697.github.io/python-flask/
"""
Created on Sat Mar  5 10:11:40 2022

@author: purem
"""
from flask import Flask, request

import socket
import requests



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


def allowed_gai_family():
    # """
    #  https://github.com/shazow/urllib3/blob/master/urllib3/util/connection.py
    # """
    family = socket.AF_INET
    return family

requests.packages.urllib3.util.connection.allowed_gai_family = allowed_gai_family
# app.config["DEBUG"] = True
app.run(host='192.168.1.106', port=80)