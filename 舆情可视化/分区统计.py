# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/5/14 11:14'
area_list=['江汉区','江夏区','硚口区','江岸区','黄陂区','新洲区','洪山区','武昌区','汉阳区','蔡甸区','武汉开发区','东西湖区','青山（化工）区']
count_list=[]
import pymongo
client = pymongo.MongoClient('127.0.0.1', 27017)  # 缺少一步骤进行属性的清洗操作，确定是否有这个值
db = client.goverment
dbname='whugover'
for i in area_list:
    count_list.append(db[dbname].find({'政府机构':i}).count())
print(count_list)