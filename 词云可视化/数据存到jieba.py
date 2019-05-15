# -*- coding: UTF-8 -*-
__author__ = 'zy'
from pyecharts import Pie
import pymongo,jieba

def show(dbname):
    client = pymongo.MongoClient('127.0.0.1', 27017)  # 缺少一步骤进行属性的清洗操作，确定是否有这个值
    db = client.goverment
    with open((dbname+'jieba'),'w+',encoding='utf-8') as f:
        for i in db[dbname].find():
            try:
                seg_list = jieba.cut(i['内容'])#, cut_all=True
                tmp=str(' '.join(seg_list))
                f.write(tmp)
                f.write('\n')
                print('写入')
            except:
                pass
    f.close()
if __name__=='__main__':
    show('whugover')

