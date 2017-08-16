# -*- coding: UTF-8 -*-

'''
Created on 2017年6月13日

@author: Caesar
'''

# import urllib
# import urllib2
# import cookielib
# 
# filename = 'cookie.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib.urlencode({
#             'form_email':'774534486@qq.com',
#             'form_password':'19971009syx'
#         })
# #登录教务系统的URL
# loginUrl = 'https://www.douban.com/accounts/login'
# #模拟登录，并把cookie保存到变量
# result = opener.open(loginUrl,postdata)
# #保存cookie到cookie.txt中
# cookie.save(ignore_discard=True, ignore_expires=True)
# #利用cookie请求访问另一个网址，此网址是成绩查询网址
# gradeUrl = 'https://www.douban.com/people/153251919/'
# #请求访问成绩查询网址
# result = opener.open(gradeUrl)
# print result.read()

import requests

s=requests.session()
postdata={'form_email':'774534486@qq.com','form_password':'19971009syx'}
res=s.post('https://www.douban.com/accounts/login', postdata)
result=s.get('http://www.douban.com/people/153251919/')
print result.text
