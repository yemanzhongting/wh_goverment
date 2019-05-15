# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/5/13 23:56'
import pymongo
import pandas as pd
import matplotlib.pyplot as plt
def show(dbname):
    client = pymongo.MongoClient('127.0.0.1', 27017)  # 缺少一步骤进行属性的清洗操作，确定是否有这个值
    db = client.goverment
    type_list=[]
    count_list=[]
    w_str=''
    with open((dbname+'day'+'.csv'),'w+',encoding='utf-8') as f:
        for i in db[dbname].find():
            try:
                tmp=i['问题时间'][0:10]+','+'1'
                f.write(tmp)
                f.write('\n' )
            except:
                pass
if __name__=='__main__':
    show('whugover')

    #####开始可视化
    x = pd.read_csv('whugoverday.csv', names=['time', 'count'], engine='python', encoding='gb18030')

    df = x.groupby(by='time').count()
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d')  # 大Y四位数
    df.plot()
    plt.show()