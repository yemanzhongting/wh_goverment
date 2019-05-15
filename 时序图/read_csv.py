# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/5/14 0:02'
import pandas as pd
import matplotlib.pyplot as plt
x=pd.read_csv('whugoverday.csv',names=['time', 'count'],engine='python',encoding='gb18030')

df=x.groupby(by='time').count()
#print(type())
#print(df['b'].head())
#
df.index=pd.to_datetime(df.index,format='%Y-%m-%d')#大Y四位数
df.plot()
plt.show()
