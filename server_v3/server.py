# 解決CORS不能瀏覽的方法
# https://blog.gtwang.org/web-development/chrome-configuration-for-access-control-allow-origin/


from flask import Flask, redirect, request, abort, send_file, render_template, url_for,send_from_directory
from datetime import datetime,timedelta
from myquery import MyRequest
import json
import socket
import requests.packages.urllib3.util.connection as urllib3_cn

from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    # return redirect('/login')
    return '<h1>Service is online!</h1>'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path),'favicon.ico', mimetype='image/vnd.microsoft.icon')

# 登入畫面
@app.route('/login/',defaults={'req_path': ''}, methods=['GET'])
@app.route('/login/<path:req_path>', methods=['GET'])
def login(req_path):
    BASE_DIR = 'server_v3\\templates'

    print('req_path:',req_path)

    if not req_path:
        req_path = 'login'

    req_path = f"{req_path}.html"

    abs_path = os.path.join(os.getcwd(),BASE_DIR)
    abs_path = os.path.join(abs_path, req_path)

    print('abs_path:',abs_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return render_template(req_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template(req_path, files=files)

# 主畫面
@app.route('/main/',defaults={'req_path': ''})
@app.route('/main/<path:req_path>')
def main(req_path):
    BASE_DIR = 'server_v3\\templates'

    print(req_path)

    if not req_path:
        req_path = 'main'

    req_path = f"{req_path}.html"

    abs_path = os.path.join(os.getcwd(),BASE_DIR)
    abs_path = os.path.join(abs_path, req_path)

    print(abs_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return render_template(req_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template(req_path, files=files)

# 主畫面
@app.route('/generator/',defaults={'req_path': ''})
@app.route('/generator/<path:req_path>')
def generator(req_path):
    BASE_DIR = 'server_v3\\templates'

    print(req_path)

    if not req_path:
        req_path = 'generator'

    req_path = f"{req_path}.html"

    abs_path = os.path.join(os.getcwd(),BASE_DIR)
    abs_path = os.path.join(abs_path, req_path)

    print(abs_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return render_template(req_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template(req_path, files=files)

# 價格面板畫面
@app.route('/monitor/',defaults={'req_path': ''})
@app.route('/monitor/<path:req_path>')
def monitor(req_path):
    BASE_DIR = 'server_v3\\templates'

    print(req_path)

    if not req_path:
        req_path = 'monitor'

    req_path = f"{req_path}.html"

    abs_path = os.path.join(os.getcwd(),BASE_DIR)
    abs_path = os.path.join(abs_path, req_path)

    print(abs_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return render_template(req_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template(req_path, files=files)

@app.route('/logout')
@app.route('/logout/')
def logout():
    return render_template("logout.html")

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

@app.route('/stockInfo', methods=['POST'])
def stockInfo():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
   
    req = json.loads(request.data)
    feedback = MyRequest(req['time'],req['stockCode'])
    
    response = feedback.GetStockInfo()
    return json.dumps(response) 


@app.route('/stockInfoV2', methods=['POST'])
def stockInfoV2():
    print("--request start--")
    print(request)
    print(request.data)
    print("--request end--")
   
    req = json.loads(request.data)
    feedback = MyRequest(req)
    print('TEST OK')
    response = feedback.GetStockInfoV3()
    return json.dumps(response) 

    

def allowed_gai_family():
    # """
    #  https://github.com/shazow/urllib3/blob/master/urllib3/util/connection.py
    # """
    family = socket.AF_INET
    return family

urllib3_cn.allowed_gai_family = allowed_gai_family




# app.add_url_rule('/favicon.ico',redirect_to=url_for('static', filename='favicon.ico'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=443, ssl_context=('C:\\SSL_TOOL\\secret\\certificate.crt', 'C:\\SSL_TOOL\\secret\\private.key'))

# print(CheckCurrentMonthData('20220326'))


