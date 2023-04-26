a = ['Action','Thriller','comedy','comedy','comedy','Action','Thriller','drama',]
b = dict.fromkeys(a,0)
dic = {}
for i in b:
    dic[i] = a.count(i)

l1 = []
for j in dic.items():
    l1.append(j)
    l1.sort(key= lambda x:x[1],reverse=True)
    top = dict(l1[0:3])
top3 = []
for m in top.keys():
    top3.append(m)
    top3_data = ','.join(top3)
print(top3_data)

