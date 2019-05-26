# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/5/26 20:08'
import pymongo
keyword_chains = {}
delimit = '\x00'

def add(keyword):
    if not isinstance(keyword ,str):
        keyword = keyword.decode('utf-8')
    keyword = keyword.lower()
    chars = keyword.strip()
    if not chars:
        return
    level = keyword_chains
    for i in range(len(chars)):
        if chars[i] in level:
            level = level[chars[i]]
        else:
            if not isinstance(level, dict):
                break
            for j in range(i, len(chars)):
                level[chars[j]] = {}
                last_level, last_char = level, chars[j]
                level = level[chars[j]]
            last_level[last_char] = {delimit: 0}
            break
    if i == len(chars) - 1:
        level[delimit] = 0

def parse(path):
    with open(path,encoding='utf-8') as f:
        for keyword in f:
            add(keyword.strip())

def filter( message, repl="*"):
    if not isinstance(message,str):
        message = message.decode('utf-8')
    message = message.lower()
    ret = []
    start = 0
    while start < len(message):
        level = keyword_chains
        step_ins = 0
        for char in message[start:]:
            if char in level:
                step_ins += 1
                if delimit not in level[char]:
                    level = level[char]
                else:
                    ret.append(repl * step_ins)
                    start += step_ins - 1
                    break
            else:
                ret.append(message[start])
                break
        else:
            ret.append(message[start])
        start += 1

    return ''.join(ret)

def get_data(dbname):
    parse(r"违禁词")

    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.goverment
    cursor=db[dbname].find({'内容':{'$exists': 'True'}})#{'comment':{'$exists': 'True'}}
    for i in cursor:

        comment=i['内容']
        data={
            "净化后":filter(comment, "*")
        }
        mongoid = i['_id']
        myquery = {"_id": mongoid}
        newvalues = {"$set":data}
        db[dbname].update_one(myquery, newvalues)
        print('改写一个')

if __name__ == "__main__":

    # parse(r"违禁词")
    # print (filter("我爱学习", "*"))
    # print (filter("针孔摄像机", "*"))
    # print (filter("售假人民币", "*"))
    # print (filter("传世私服", "*"))
    get_data('whugover')