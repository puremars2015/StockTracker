

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Welcome to Theta Information !</h1>'



app.run(host='220.133.234.2', port=80)