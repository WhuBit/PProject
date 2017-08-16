# ---coding:utf-8---

with open('E:\\cinema_pro.txt','r') as f1:
    cp={}
    index=1
    for line in f1:
        if(index%2!=0):
            line=line.strip().decode('utf-8')
            ss=line.split('\t')
            cp[ss[1]]=ss[8]
            print ss[1].encode('utf-8'),cp[ss[1]].encode('utf-8')
        index=index+1
    f1.close

index=0
with open('E:\\movie_cinema_2016.txt','r') as f2:
    f3=open('E:\\movie_cinema_2016n.txt','a')
    for line in f2:
        line=line.strip().decode('utf-8')
        ss=line.split('\t')
        if(cp.has_key(ss[2])):
            print line.encode('utf-8')+'\t'+cp[ss[2]].encode('utf-8')
            f3.write(line.encode('utf-8')+'\t'+cp[ss[2]].encode('utf-8')+'\n')
            index=index+1
        else:
            print 'no'
    print 'end:'+str(index)
    


