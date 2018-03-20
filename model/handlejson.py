# coding=UTF-8

from flask import Flask, render_template, request, send_file, jsonify, session
from flaskext.markdown import Markdown
from flask_cors import *
import json
import xlrd

def writejson():
    workbook = xlrd.open_workbook("model\\dict.xlsx")
    worksheet = workbook.sheet_by_name("Sheet1")
    data = []
    keys = [v.value for v in worksheet.row(0)]
    for row_number in range(worksheet.nrows):
        if row_number == 0:
            continue
        row_data = {}
        for col_number, cell in enumerate(worksheet.row(row_number)):
            row_data[keys[col_number]] = cell.value
        data.append(row_data)

    with open("model\\dict.json",'w') as json_file:
        json_file.write(json.dumps({'data': data}))


def readjson():
    with open("model\\dict.json",'rb') as modjs:
        words = json.load(modjs)
    return words


def queryjson(qword):
    # readxls()
    words=readjson()
    rlt=[]
    word=qword.strip()
    for i,val in enumerate(words["data"]):
        if word in val["中文"]:
            rlt.append(val)
        elif word in val["法文"]:
            rlt.append(val)
        elif word in val["藏文"]:
            rlt.append(val)
        elif word in val["汉语拼音"]:
            rlt.append(val)
        elif word in val["梵文"]:
            rlt.append(val)
    return rlt
        # elif word==val["巴利文"]:
        #     rlt="巴利文"
        # elif word==val["日文"]:
        #     rlt="日文"
        # elif word==val["韩文"]:
        #     rlt="fr"
        # elif word==val["英文"]:
        #     rlt="fr"
        # elif word==val["德文"]:
        #     rlt="fr"
        # elif word==val["俄文"]:
        #     rlt="fr"
        # elif word==val["西班牙语"]:
        #     rlt="fr"
        # elif word==val["泰语"]:
        #     rlt="fr"
        # elif word==val["葡萄牙语"]:
        #     rlt="fr"        
        # elif word==val["荷兰语"]:
        #     rlt="fr"   
        # elif word==val["越南语"]:
        #     rlt="fr"  
# print(query("达"))
