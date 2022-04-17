import sqlite3
import json
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


print(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'


@app.route('/login', methods=["POST"])
def login():
    return "OK!"


@app.route('/stockInfo', methods=['POST'])
def stockInfo():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    obj = json.loads(data)
    

    
    
    print(obj)
    print(type(obj))
    print(obj['stockCode'])
    

    #print(request.header)
    print(request.headers['Token'])
    
    

    return "OK!"

app.run(host='220.133.234.2', port=80)