# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            line=item.split('=')
            key = line[0].replace(' ', '')
            value = line[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = 'll="118254"; bid=-8r4hwPy5pg; gr_user_id=332bd683-3ba0-42f7-a958-4f2a7ba15e84; viewed="1455616_2365393_5386062_6792322_6523997_26704403"; ps=y; _vwo_uuid_v2=08D028446FDD6EB4111B21A3DFFDC7DD|b9d78bfdea484a87e451712dc5cff4dc; ap=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1499344677%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; __utmt=1; _ga=GA1.2.1416774594.1491391687; _gid=GA1.2.1093756690.1499344733; _gat_UA-7019765-1=1; dbcl2="153251919:9XJ4GHwUug4"; ck=RQPN; _pk_id.100001.8cb4=f976e6bd2852870d.1491391682.14.1499344747.1499306796.; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utma=30149280.1416774594.1491391687.1499306797.1499344678.24; __utmb=30149280.3.10.1499344678; __utmc=30149280; __utmz=30149280.1499344678.24.16.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=30149280.15325'
    trans = transCookie(cookie)
    print trans.stringToDict()