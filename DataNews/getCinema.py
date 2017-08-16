# ---coding:utf-8---

with open('E:\\cinema1.txt','r') as f1:
    cinema=[]
    for line in f1:
        line=line.strip().decode('utf-8')
        cinema.append(line)
print len(cinema)

f3=open('E:\\cinema_pro_n.txt','w')
with open('E:\\cinema_pro.txt','r') as f2:
    index=1
    for line in f2:
        if(index%2!=0):
            line=line.strip().decode('utf-8')
            ss=line.split('\t')
            if ss[1] in cinema:
                print line.encode('utf-8')
                f3.write(line.encode('utf-8')+'\n')
        index=index+1
print 'end'