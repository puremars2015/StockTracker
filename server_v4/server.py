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
@app.route('/login')
@app.route('/login/')
def login():
    return render_template("login.html")

# 主畫面
@app.route('/main/',defaults={'action': ''})
@app.route('/main/<path:action>')
def main(action):

    print("action:", action)

    BASE_DIR = 'server_v4\\templates'
    filePath = f"{action}.html"
    fileFullPath = os.path.join(os.getcwd(),BASE_DIR)
    fileFullPath = os.path.join(fileFullPath, filePath)

    # Check if path is a file and serve
    if os.path.isfile(fileFullPath):
        return render_template("main.html")
    return render_template("main.html")



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

@app.route('/monitor')
@app.route('/monitor/') 
def monitor():
    return render_template("monitor.html")

def allowed_gai_family():
    # """
    #  https://github.com/shazow/urllib3/blob/master/urllib3/util/connection.py
    # """
    family = socket.AF_INET
    return family

urllib3_cn.allowed_gai_family = allowed_gai_family



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=443, ssl_context=('C:\\SSL_TOOL\\secret\\certificate.crt', 'C:\\SSL_TOOL\\secret\\private.key'))


