#-*- coding: UTF-8 -*- 

f3=open('E:\movie_other.txt','w')

with open('E:\movie_name.txt','r') as f1:
    for line1 in f1:
        line1=line1.strip()
        flag=0;
        f2=open('E:\\all_movie.txt','r')
        for line2 in f2:
            line2=line2.strip().split('\t')
            print line1,line2[0]
            if cmp(line1,line2[0])==0:
                flag=1;
                break;
        f2.close
        if flag==0:
            print line1+'\n'
            f3.write(line1+'\n')
print 'end'

f3.close

