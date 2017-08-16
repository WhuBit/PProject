#-*- coding:UTF-8 -*-

'''
Created on 2017年5月4日

@author: Caesar
'''

from __future__ import division
import os

fopen=open('E:\\OneDrive\\Documents\\decimal.txt','w')

for i in range(1,100):
    for j in range(1,i):
        fopen.write('%s,%s\n'%(str(j)+'/'+str(i),j/i))

fopen.close()
