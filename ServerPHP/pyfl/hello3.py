# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: hello.py
@time: 2017/11/29 22:15
@项目名称:operating
"""

import urllib.request

import urllib.parse
# requests库的http请求、
"""
　①get请求：requests.get(‘url‘) 
　　②post请求：requests.post("url/post")
　　③put请求：requests.put("url/put")
　　④delete请求：requests.delete("url/delete")
　　⑤head请求：requests.head("url/get")
　　⑥options请求：requests.options("url/get")
"""
import requests
import time


class user_class(object):
    args = {}
    date = ""
    files = ""
    form = {}
    headers = {}
    json = ""
    origin = ""
    url = ""


import json
class kk ():
    def obj_test(self, result, obj):
        data_list = []
        for res in result:
            test = obj
            dictionaries = {}
            jsondatar = json.dumps(res, ensure_ascii=False)
            rebuild = json.loads(jsondatar)
            print(" rebuild %s" % rebuild)
            test.__dict__ = rebuild
            dictionaries[test.key] = test
            print(" test %s" % test )
            print(" test.id %s" % test.key )
            data_list.append(dictionaries)
        return data_list;

class qu():
    key = ""
    info = ""

if __name__ == '__main__':

    url = 'http://www.baidu.com'

    r = requests.get(url)

    print(r.headers)  # 打印运行信息
    print(r.elapsed.microseconds)  # 打印运行时间

    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://httpbin.org/post", data=payload)
    print(r.text)
    s = kk()
    time.sleep(2)
    date = {"key": "your", "info": '你好'}

    s.obj_test(date, qu())
