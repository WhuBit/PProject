# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class MyscrapyPipeline(object):
    def process_item(self, item, spider):
        print u'写入准备...'
        f = open('E:\info.txt', 'a')
        info = u"%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (
            item['name'], item['year'], item['directors'],  item['actors'],
            item['genres'], item['countries'], item['average'])
        f.write(info.encode('utf-8'))
        f.close()

        return item
