# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MovieItem(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    directors = scrapy.Field()
    actors = scrapy.Field()
    genres = scrapy.Field()
    countries = scrapy.Field()
    average = scrapy.Field()