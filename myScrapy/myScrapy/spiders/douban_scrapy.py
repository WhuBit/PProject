# -*- coding: utf-8 -*-

import json
import scrapy
from myScrapy.items import MovieItem

class MoviesSpider(scrapy.Spider):
    name = "Movie"
    allowed_domains = ["https://api.douban.com/v2/movie/"]
    meta = {
        'dont_redirect': True,
        'handle_httpstatus_list': [301, 302]
    }

    def start_requests(self):
        f1 = open(r'E:\url2.txt')
        for line in f1:
            url = 'https://api.douban.com/v2/movie/' + line.strip()
            yield scrapy.Request(url, callback=self.parse, meta=self.meta)

    def parse(self, response):
        js = json.loads(response.body)
        item = MovieItem()
        item['name'] = js['title']
        item['average'] = js['rating']['average']
        item['genres'] = ''
        try:
            for one in js['attrs']['movie_type']:
                item['genres'] += one+','
        except:
            item['genres']=None;
        item['countries'] = ''
        for one in js['attrs']['country']:
            item['countries'] += one+','
        item['directors'] = ''
        for one in js['attrs']['director']:
            item['directors'] += one + ','
        item['actors'] = ''
        try:
            for one in js['attrs']['cast']:
                item['actors'] += one + ','
        except:
            item['actors']=None
        for one in js['attrs']['year']:
            item['year'] = one

        yield item
