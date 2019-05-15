# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)

import matplotlib.pyplot as plt
import pymongo
problem_list=[]

import heapq

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.goverment
dbname='whugover'
cursor=db[dbname].find()
for i in cursor:
    for j in i['问题分类列表']:
        if j not in problem_list:
            problem_list.append(j)

#返回所有问题列表
count_problem_list=[]
tmp_list=[]

cursor=db[dbname].find()
for i in cursor:
    for j in i['问题分类列表']:
        tmp_list.append(j)

for tmp in problem_list:
    count_problem_list.append(tmp_list.count(tmp))

print(problem_list[0:12])
print(count_problem_list[0:12])

max_num_index_list = map(count_problem_list.index, heapq.nlargest(20, count_problem_list))
max_list=list(max_num_index_list)[0:7]

t_=[]
t_count=[]
for i in max_list:
    t_.append(problem_list[i])
    t_count.append(count_problem_list[i])


plt.bar(t_,t_count, label='词频')


# params

# x: 条形图x轴
# y：条形图的高度
# width：条形图的宽度 默认是0.8
# bottom：条形底部的y坐标值 默认是0
# align：center / edge 条形图是否以x轴坐标为中心点或者是以x轴坐标为边缘

plt.legend()

plt.xlabel('词语')
plt.ylabel('频次')

plt.title(u'词频条形图', FontProperties=font)

plt.show()