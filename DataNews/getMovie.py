# ---coding:utf-8---

with open('E:\\all_movie_n.txt','r') as f1:
    movie=[]
    for line in f1:
        line=line.strip().decode('utf-8')
        ss=line.split('\t')
        movie.append(ss[0])

with open('E:\\movie.txt','r') as f2:
    for line in f2:
        line=line.strip().decode('utf-8')
        ss=line.split('\t')
        if ss[0] not in movie:
            print line.encode('utf-8')
print 'end'