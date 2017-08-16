#coding=utf-8

import jieba
import jieba.posseg as pseg
jieba.set_dictionary('D:\\Python27\\extra\\dict.txt.big.txt')

f=open('E:\\OneDrive\\Documents\\学习资料\\信息组织\\林夕歌词(张国荣、杨千嬅、陈奕迅).txt'.decode("utf-8"),'r')
text=f.read()

words=pseg.cut(text)
for word,flag in words:
    if(flag=='a'):
        f=open('E:\\OneDrive\\Documents\\学习资料\\信息组织\\a.txt'.decode("utf-8"),'a')
        f.write(word.encode("utf-8")+'\n')
    elif(flag=='nr'):
        f=open('E:\\OneDrive\\Documents\\学习资料\\信息组织\\nr.txt'.decode("utf-8"),'a')
        f.write(word.encode("utf-8")+'\n')
    elif(flag=='ns'):
        f=open('E:\\OneDrive\\Documents\\学习资料\\信息组织\\ns.txt'.decode("utf-8"),'a')
        f.write(word.encode("utf-8")+'\n')
    elif(flag=='v'):
        f=open('E:\\OneDrive\\Documents\\学习资料\\信息组织\\v.txt'.decode("utf-8"),'a')
        f.write(word.encode("utf-8")+'\n')

print "end"
f.close()
