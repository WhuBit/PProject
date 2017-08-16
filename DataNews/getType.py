# ---coding:utf-8---

with open('E:\\all_movie.txt','r') as f1:
    mt={}
    index=1
    for line in f1:
        line=line.strip().decode('utf-8')
        if(index!=1):
            ss=line.split('\t')
            mt[ss[0]]=ss[1]
        index=index+1
    for (k,v) in mt.items():
        print '%s:%s'%(k.encode('utf-8'),v.encode('utf-8'))
    print len(mt)
    f1.close

f3=open('E:\movie_cinema_2016n.txt','w')
str='id\tcinema_id\tcinema_name\tdate\tmovie_name\tbox_office_now\tbox_office_accounting\trow_accounting\tbox_office_total\tpro\ttype\n'.decode('utf-8')
print str
f3.write(str.encode('utf-8'))
with open('E:\\movie_cinema_2016.txt','r') as f1:
    for line in f1:
        line=line.strip().decode('utf-8')
        ss=line.split('\t')
        print line.encode('utf-8')+'\t'+mt[ss[4]].encode('utf-8')
        f3.write(line.encode('utf-8')+'\t'+mt[ss[4]].encode('utf-8')+'\n')
print 'end'
