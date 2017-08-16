# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random

import requests

from myScrapy.settings import IPPOOL


class RandomUserAgent(object):
    """根据预定义的列表随机更换用户代理"""
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))
        
class MyproxiesSpiderMiddleware(object):
    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        thisip = random.choice(IPPOOL)
        url = 'https://api.douban.com/v2/movie/subject/10001352'
        while((requests.get(url,proxies = thisip).status_code)!=200):
            thisip = random.choice(IPPOOL)
        print("this is ip:" + thisip["ipaddr"])
        request.meta["proxy"] = "http://" + thisip["ipaddr"]