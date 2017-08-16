#-*- coding: UTF-8 -*- 

with open('E:\敦煌\Q-文本\TQ.txt'.decode('utf-8'),'r') as f1:
    print 'start!'
    for line in f1:
        print line
        line=line.strip().decode('utf-8')
        ss=line.split('\t')
        f2=open('E:\敦煌\Q-文本\T'.decode('utf-8')+ss[1]+'.txt','w')
        print ss;
        f2.write(ss[2].encode('utf-8')+'\n')
        f2.close
    print 'end'
    f1.close