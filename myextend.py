#!/usr/bin/env python
# -- coding: utf-8 --
import time
import threading

import requests
from scrapy import signals

# 提取代理IP的api
api_url = 'https://dps.kdlapi.com/api/getdps/?secret_id=obhjaa78z35bua1hwrnw&signature=i8x8hopc214dignrx908x7wixo00ypwe&num=1&format=text&sep=1'
foo = True

class Proxy:

    def __init__(self, ):
        #self._proxy_list = requests.get(api_url).json().get('data').get('proxy_list')
        # 修改JSON解析为文本解析
        response = requests.get(api_url)
        proxy_text = response.text.strip()
        if proxy_text:
            self._proxy_list = proxy_text.split('\n')
        else:
            self._proxy_list = []
    @property
    def proxy_list(self):
        return self._proxy_list

    @proxy_list.setter
    def proxy_list(self, list):
        self._proxy_list = list


pro = Proxy()
print('代理列表数量：',len(pro.proxy_list))
print('代理列表：',pro.proxy_list)


class MyExtend:

    def __init__(self, crawler):
        self.crawler = crawler
        # 将自定义方法绑定到scrapy信号上,使程序与spider引擎同步启动与关闭
        # scrapy信号文档: https://www.osgeo.cn/scrapy/topics/signals.html
        # scrapy自定义拓展文档: https://www.osgeo.cn/scrapy/topics/extensions.html
        crawler.signals.connect(self.start, signals.engine_started)
        crawler.signals.connect(self.close, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def start(self):
        t = threading.Thread(target=self.extract_proxy)
        t.start()

    def extract_proxy(self):
        '''while foo:
            pro.proxy_list = requests.get(api_url).json().get('data').get('proxy_list')
            #设置每15秒提取一次ip

            time.sleep(15)'''
        while foo:
            # 修改JSON解析为文本解析
            response = requests.get(api_url)
            proxy_text = response.text.strip()
            if proxy_text:
                pro.proxy_list = proxy_text.split('\n')
            else:
                pro.proxy_list = []
            # 设置每15秒提取一次ip
            time.sleep(15)
    def close(self):
        global foo

        foo = False

#原json解析出错
