# 解決CORS不能瀏覽的方法
# https://blog.gtwang.org/web-development/chrome-configuration-for-access-control-allow-origin/

import json
from flask import Flask, request, abort, send_file, render_template,url_for
from datetime import datetime,timedelta
from dbhelper import DbHelper
from myquery import MyRequest


import socket
import requests.packages.urllib3.util.connection as urllib3_cn

from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)

def WriteData(message,symbol):
    db = DbHelper('tradingview.db','ALERTMESSAGE')

    if not db.IsInit():
        db.CreateAlertMessage()
        db.InitAlertMessage()
        
    idx = db.GetID()
    
    db.WriteAlertMessage(idx + 1, message, symbol, datetime.now())
    
def WriteThreeBig(unit, buy, sell, diff, date):
    db = DbHelper('tradingview.db','THREE_BIG')
    
    if not db.IsInit():
        db.CreateThreeBig()
        db.InitThreeBig()
        
    idx = db.GetID()
    
    db.WriteThreeBig(idx + 1, unit, buy, sell, diff, date, datetime.now())
    
def CheckCurrentMonthData(date):
    db = DbHelper('tradingview.db','THREE_BIG')
    
    endDate = datetime.strptime(date, '%Y%m%d')
    startDate = endDate + timedelta(days=-endDate.day+1)
    
    print(startDate,endDate)
    
    emptydays = db.CheckSelfBusinessTradeBySelf(startDate.strftime('%Y%m%d'), endDate.strftime('%Y%m%d'))
    
    print(emptydays)
    
    return emptydays

def ReadThreeBigByMonth(date):
    db = DbHelper('tradingview.db','THREE_BIG')
    
    endDate = datetime.strptime(date, '%Y%m%d')
    startDate = endDate + timedelta(days=-endDate.day+1)
    
    return db.ReadSelfBusinessTradeBySelf(startDate.strftime('%Y%m%d'), endDate.strftime('%Y%m%d'))


@app.route('/')
def hello_world():
    return '<h1>Welcome to Theta Information !</h1>'

@app.route('/favicon.ico/')
def favicon():
    
    return
    

@app.route('/sample/',defaults={'req_path': ''})
@app.route('/sample/<path:req_path>')
def index(req_path):
    BASE_DIR = 'C:/Users/purem/Desktop/stock_tracking_system/project'

    print(req_path)

    if not req_path:
        req_path = 'index.html'

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template('index.html', files=files)



# @app.route('/', defaults={'req_path': ''})
# @app.route('/sample/<path:req_path>')
# def dir_listing(req_path):
#     BASE_DIR = 'C:/Users/purem/Desktop/stock_tracking_system/project'

#     # Joining the base and the requested path
#     abs_path = os.path.join(BASE_DIR, req_path)

#     # Return 404 if path doesn't exist
#     if not os.path.exists(abs_path):
#         return abort(404)

#     # Check if path is a file and serve
#     if os.path.isfile(abs_path):
#         return send_file(abs_path)

#     # Show directory contents
#     files = os.listdir(abs_path)
#     return render_template('index.html', files=files)

@app.route('/.well-known/pki-validation/B87B968F8367A7B79753D5221B1BFDD0.txt')
def identify():
    with open('C:\SSL_TOOL\key\B87B968F8367A7B79753D5221B1BFDD0.txt') as f:
        lines = f.read()
        print(lines)
    return lines

@app.route('/stock-sample')
def stockapp():
    with open('C:/Users/purem/Desktop/stock_tracking_system/project/index.html') as f:
        lines = f.read()
        print(lines)
    return

@app.route('/signal_us500')
def getSignalUs500():
    db = DbHelper('tradingview.db','ALERTMESSAGE')
    signal = db.ReadUs500()
    print(signal)
    return signal

@app.route('/login', methods=["POST"])
def login():
    return "OK!"

@app.route('/stockInfo', methods=['POST'])
def stockInfo():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
   
    req = json.loads(request.data)
    
    print(req,req['stockCode'],req['time'])
    
    feedback = MyRequest(req['time'],req['stockCode'])
    
    response = feedback.GetStockInfo()
    
    print(response)
    return json.dumps(response) 
    # return "OK!"

@app.route('/stockInfoV2', methods=['POST'])
def stockInfoV2():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
   
    req = json.loads(request.data)
    
    print(req,req['stockCode'],req['time'])
    
    feedback = MyRequest(req['time'],req['stockCode'])
    
    response = feedback.GetStockInfoV2()
    
    print(response)
    return json.dumps(response) 

@app.route('/threeBig', methods=['POST'])
def threeBig():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
   
    req = json.loads(request.data)
    
    print(req,req['stockCode'],req['time'])
    
    feedback = MyRequest(req['time'],req['stockCode'])
    
    response = feedback.GetThreeBig()
    
    print(response)   
    return response

@app.route('/threeBigMonth', methods=['POST'])
def threeBigMonth():
    print("--request start--")
    print(request)
    print(request.json)
    print("--request end--")

    req = request.json
    
    # 檢查日期當月資料是否都有
    checkResult = CheckCurrentMonthData(req['time'])
    # print(checkResult)
    # 如果有日期,表示該日期有缺資料
    
    # print('checking data')
    
    if len(checkResult) != 0:
        feedback = MyRequest(req['time'],req['stockCode'])
        # response = feedback.GetThreeBig()
        # print(response)
        
        for i in checkResult:
            # print("---",i,"---")
            feedback.date = i
            response = feedback.GetThreeBig()
            # print(response)            
            # print("----write data----")
            
            datas = response['data']
            
            for row in datas:
                # print(row[0],row[1],row[2],row[3],response['date'])
                WriteThreeBig(row[0],row[1],row[2],row[3],response['date'])
            
            
            # print("----write data complete----")          
            # print("---",i,"complete","---")
            

    # print('checking data complete')
    return json.dumps(ReadThreeBigByMonth(req['time']))
    

@app.route('/webhook_bitcoin', methods=['POST'])
def webhook_bitcoin():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'bitcoin')
    
    return "OK!"
    
@app.route('/webhook_us500_d1', methods=['POST'])
def webhook_us500_d1():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'us500_d1')
    
    return "OK!"

@app.route('/webhook_us500_h4', methods=['POST'])
def webhook_us500_h4():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'us500_h4')
    
    return "OK!"
    
@app.route('/webhook_us500_h2', methods=['POST'])
def webhook_us500_h2():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'us500_h2')
    
    return "OK!"

@app.route('/webhook_us500_h1', methods=['POST'])
def webhook_us500_h1():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'us500_h1')
    
    return "OK!"
        
@app.route('/webhook_us500_m5', methods=['POST'])
def webhook_us500_m5():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'us500_m5')
    
    return "OK!"

@app.route('/webhook_us500_m5_2', methods=['POST'])
def webhook_us500_m5_2():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'us500_m5_2')
    
    return "OK!"

@app.route('/webhook_nas100_d1', methods=['POST'])
def webhook_nas100_d1():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'nas100_d1')
    
    return "OK!"

@app.route('/webhook_nas100_h4', methods=['POST'])
def webhook_nas100_h4():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'nas100_h4')
    
    return "OK!"

@app.route('/webhook_nas100_h2', methods=['POST'])
def webhook_nas100_h2():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'nas100_h2')
    
    return "OK!"

@app.route('/webhook_nas100_h1', methods=['POST'])
def webhook_nas100_h1():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'nas100_h1')
    
    return "OK!"

@app.route('/webhook_qqq_d2', methods=['POST'])
def webhook_qqq_d2():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'qqq_d2')
    
    return "OK!"

@app.route('/webhook_qqq_d1', methods=['POST'])
def webhook_qqq_d1():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'qqq_d1')
    
    return "OK!"

@app.route('/webhook_qqq_h4', methods=['POST'])
def webhook_qqq_h4():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'qqq_h4')
    
    return "OK!"

@app.route('/webhook_spy_d2', methods=['POST'])
def webhook_spy_d2():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'spy_d2')
    
    return "OK!"

@app.route('/webhook_spy_d1', methods=['POST'])
def webhook_spy_d1():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'spy_d1')
    
    return "OK!"

@app.route('/webhook_spy_h4', methods=['POST'])
def webhook_spy_h4():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
    
    data = request.data.decode('utf-8')
    print(data)
    WriteData(data, 'spy_h4')
    
    return "OK!"


def allowed_gai_family():
    # """
    #  https://github.com/shazow/urllib3/blob/master/urllib3/util/connection.py
    # """
    family = socket.AF_INET
    return family

urllib3_cn.allowed_gai_family = allowed_gai_family

# app.add_url_rule('/favicon.ico',redirect_to=url_for('static', filename='favicon.ico'))

# if __name__ == "__main__":
#     app.run(host='220.133.234.2', port=443, ssl_context=('C:\\SSL_TOOL\\secret\\certificate.crt', 'C:\\SSL_TOOL\\secret\\private.key'))

# print(CheckCurrentMonthData('20220326'))


