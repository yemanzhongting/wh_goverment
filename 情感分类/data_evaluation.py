#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from snownlp import SnowNLP
#from snownlp.sentiment import Sentiment
import matplotlib.pyplot as plt
import pymongo,jieba
comment = []
pos_count = 0
neg_count = 0

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.goverment
dbname='whugover'
#('whugover')
pos_count=db[dbname].find({'情感':'积极'}).count()
neg_count=db[dbname].find({'情感':'消极'}).count()
#\n(eg. pray,eulogize and suggestion)   \n(eg. abuse,sarcasm and indignation)
labels = 'Positive Side', 'Negative Side'
fracs = [pos_count,neg_count]
explode = [0.1,0] # 0.1 凸出这部分，
plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
#autopct ，show percet

plt.pie(x=fracs, labels=labels, explode=explode,autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6)

plt.savefig("emotions_pie_chart.jpg",dpi = 360)
plt.show()
