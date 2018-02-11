import urllib
import os
import datetime
import pandas as pd
import numpy as np
import tushare as ts
import csv
import json
import matplotlib.pyplot as plt
import time

# -*- coding: utf-8 -*-
def ts_get_stock(x):
	stockid = x['stockid']
	sdate = x['sdate']
	edate = x['edate']
	# os.remove('static/stock.png')
	stockdata = ts.get_k_data(stockid, start=sdate, end=edate)
	stockname = ts.get_realtime_quotes(stockid)
	stockdata = stockdata.to_dict('records')
	stockname = stockname.to_dict('records')
	stockname = stockname[0]['name']
	# stockdata.to_json('stockid.csv')
	# csvfile = open('stockid.csv', 'r')
	# reader = csv.DictReader( csvfile )
	# out = json.dumps( [ row for row in reader ] )
	for rd in stockdata:
	    if float(rd['open'])<= float(rd['close']):
	        rd['up']= 1
	    else:
	        rd['up']= -1 
	    rd['scope']=int(rd['up'])*(float(rd['high'])-float(rd['low'])) / float(rd['low'])*100
	#     del rd['code']
	#     del rd['close']
	#     del rd['open']
	#     del rd['high']
	#     del rd['low']
	#     del rd['volume']
	plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
	plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
	ax = plt.subplot()
	ax.bar(range(len(stockdata)), [t['scope'] for t in stockdata]  , align="center")
	# ax.set_xticklabels([t['date'] for t in stockdata], rotation=90)
	plt.xlabel(u"时间")
	plt.ylabel(u"(最高价-最低价）/ 最低价 x 100%")
	plt.title(stockname+u"股价波动示意图")
	trick = "static/" + int(time.time()).__str__() + '.png'
	plt.savefig(trick)
	plt.gcf().clear()

	return [stockname,stockdata,trick]


def retrive_stock_data(stockid):
    """ 下载整个股票数据 """

    # print('downloading %s to %s' % (stockid, folder))
    url = 'http://table.finance.yahoo.com/table.csv?s=%s' % (stockid)
    # fname = os.path.join(folder, '%s.csv' % stockid.split('.')[0])
    # if not os.path.isdir(folder):
    #     os.mkdir(folder)
    fname = 'stock.csv'
    urllib.urlretrieve(url, fname)


def update_stock_data(stockid, folder):
    """ 更新股票数据，如果不存在，则下载。如果存在，则只更新最近日期的数据 """

    fname = os.path.join(folder, '%s.csv' % stockid.split('.')[0])
    if not os.path.exists(fname):
        retrive_stock_data(stockid, folder)
        return

    data = pd.read_csv(fname, index_col='Date', parse_dates=True)

    last_date = data.iloc[0:1].index.tolist()[0]
    today = pd.Timestamp(datetime.date.today())
    if today - last_date < pd.Timedelta(days=2):
        print('Nothing to update. %s last date is %s.' % (stockid, last_date))
        return

    print('updatting %s to from %s to %s' % (stockid, last_date.date(), today.date()))
    query = [
        ('a', last_date.month - 1),
        ('b', last_date.day),
        ('c', last_date.year),
        ('d', today.month - 1),
        ('e', today.day),
        ('f', today.year),
        ('s', stockid),
    ]
    url = 'http://table.finance.yahoo.com/table.csv?%s' % urllib.urlencode(query)
    temp_file = fname + '.tmp'
    urllib.urlretrieve(url, temp_file)
    update_data = pd.read_csv(temp_file, index_col='Date', parse_dates=True)
    data = data.append(update_data)
    data.sort_index(ascending=False, inplace=True)
    data.to_csv(fname, mode='w')
    os.unlink(temp_file)


def stock_list(files, postfixs):
    """ 合并股票列表，输出合并后的，可以通过 yahoo api 获取的股票列表

    files: a sequence like ['SH.txt', 'SZ.txt']
    postfixs: a sequence map to files, like ['.ss', '.sz']
    """
    if len(files) != len(postfixs):
        print('error: size of files and postfixs not match.')
        return

    stocks = []
    for i in range(len(files)):
        data = pd.read_csv(files[i], header=None, names=['name', 'id'], stockdataype={'id': np.string0})
        data['postfix'] = postfixs[i]
        stocks.append(data)

    data = pd.concat(stocks)
    print('%d files. %d stocks.' % (len(files), len(data)))
    return data


def update_stock_data_batch():
    """ 批量更新所有股票数据 """

    slist = stock_list(['SH.txt', 'SZ.txt'], ['.ss', '.sz'])
    for i in range(len(slist)):
        s = slist.iloc[i]
        update_stock_data(s['id'] + s['postfix'], 'yahoo-data')