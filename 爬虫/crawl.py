# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/5/10 18:47'
import requests
import re,random,time
import requests
from lxml import etree
import pymongo
from snownlp import SnowNLP

#分析留言详情页页面规律
#http://liuyan.cjn.cn/threads/content?tid=100001
def data_crawl(dbname):
    client = pymongo.MongoClient('127.0.0.1', 27017)  # 缺少一步骤进行属性的清洗操作，确定是否有这个值
    db = client.goverment
    start_url='http://liuyan.cjn.cn/threads/content?tid={id}'
    header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
            }
    count_num=1
    #111132断点抓取100001
    for i  in range(100001,300001):
        tmp=start_url.format(id=i)
        print(tmp)

        try:
            req=requests.get(tmp,headers=header,timeout=(3,7))
            if req.status_code==500:
                pass
            elif req.status_code==200:
                selector = etree.HTML(req.content)

                name=selector.xpath('/html/body/div[6]/h2/b/text()')[0].strip()

                condition='/html/body/div[6]/h2/b/em/text()'#记得消除空格
                condition=selector.xpath(condition)[0].strip()

                content='//*[@id="zoom"]/text()'
                content=selector.xpath(content)[0]

                problem_time='/html/body/div[6]/h3/span/text()'
                problem_time=selector.xpath(problem_time)[0][-16:]

                problem_cluster='/html/body/div[6]/h3/em/a/text()'#有多个
                problem_cluster=selector.xpath(problem_cluster)

                problem_cluster_list=problem_cluster
                new_tmp=''
                for tmp in problem_cluster:
                    new_tmp+=tmp+','#逗号分隔
                problem_cluster=new_tmp

                try:
                    unit='/html/body/div[7]/ul/li/h3/em/text()'#只有一个，两个一样的xpath，需要字符串处理

                    ss=selector.xpath(unit)[0]
                    split_ss=ss.split('\n                            \n')

                    unit=split_ss[0].strip()[5:]
                    reply_time=split_ss[1].strip()

                    reply_content='/html/body/div[7]/ul/li/p/text()'
                    reply_content=' '.join(selector.xpath(reply_content))

                    data = {
                        '标题': name,
                        '回复状态': condition,
                        '内容': content,
                        '问题时间': problem_time,
                        '问题分类': problem_cluster,
                        '问题分类列表':problem_cluster_list,
                        '政府机构': unit,
                        '回复时间': reply_time,
                        '回复内容': reply_content
                    }
                except:
                    data = {
                        '标题': name,
                        '回复状态': condition,
                        '内容': content,
                        '问题时间': problem_time,
                        '问题分类': problem_cluster,
                        '问题分类列表': problem_cluster_list,
                        '政府机构': '',
                        '回复时间': '',
                        '回复内容': ''
                    }
                ##添加情感分析模块
                s = SnowNLP(content)
                rates = s.sentiments
                if (rates >= 0.5):
                    data['情感'] = '积极'

                elif (rates < 0.5):
                    data['情感'] = '消极'

                db[dbname].insert_one(data)
                print('插入一条'+str(count_num))
                count_num+=1
        except Exception as e:
            time.sleep(1)
            print("未知错误", e)
        #如果没有抓取Status Code: 500
        #s.strip()

if __name__=='__main__':
    data_crawl('武汉市政府')