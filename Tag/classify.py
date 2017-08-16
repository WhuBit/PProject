# -*- coding: UTF-8 -*-

'''
Created on 2017年6月5日

@author: Caesar
'''

import MySQLdb

try:
    print "开始连接..."
    db=MySQLdb.connect("localhost","root","1997syx","tag",3306)
    print "连接成功"
    cur=db.cursor()
    print "正在执行..."
    cur.execute("SELECT DISTINCT url FROM sd ORDER BY url INTO OUTFILE 'E:\\\Tag\\\url.txt' LINES TERMINATED BY '\\r\\n'")
    db.commit()
    print "已提交"
    cur.close()
    print "cur已关闭"
    db.close()
    print "ִ执行完毕"

except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
