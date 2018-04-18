from flask import Flask, render_template, request, send_file, jsonify, session
from markdown import Markdown
from flask_cors import *
from model.handlejson import writejson, readjson, queryjson
import json
import xlrd


app = Flask(__name__)
CORS(app,supports_credentials=True)

#--------------------移动端---------------------------

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    rlt = ""
    u=request.args.get("user")
    p=request.args.get("password")
    if u=="admin" and p=="841110":
        rlt = "admin"
    elif u=="user" and p=="fyzx":
        rlt = "user"
    else:
        rlt = "error"
    return rlt

@app.route('/query')
def query():
    word=request.args.get("word")
    rlt=queryjson(word)
    num=len(rlt)
    return render_template("result.html",rlt=rlt,word=word,num=num)


@app.route('/admin/<method>')
def admin(method):
    if method=='restart':
        writejson()
        return 'dict restarted!'

#--------------------主程序---------------------------

if __name__ == '__main__':
    app.secret_key="19811015"

    app.run(host='0.0.0.0', port=80,debug=True)
