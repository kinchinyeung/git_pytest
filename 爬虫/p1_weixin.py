#coding:utf-8
import requests as rq
url='http://rate.tmall.com/list_detail_rate.htm?itemId=41464129793&sellerId=1652490016¤tPage=1'
myweb = rq.get(url)

import re
myjson = re.findall('\"rateList\":(\[.*?\])\,\"tags\"',myweb.text)[0]

import pandas as pd
mytable = pd.read_json(myjson)


