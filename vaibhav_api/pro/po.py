# a = ['Action','Thriller','comedy','comedy','comedy','Action','Thriller','drama',]
# b = dict.fromkeys(a,0)
# dic = {}
# for i in b:
#     dic[i] = a.count(i)

# l1 = []
# for j in dic.items():
#     l1.append(j)
#     l1.sort(key= lambda x:x[1],reverse=True)
#     top = dict(l1[0:3])
# top3 = []
# for m in top.keys():
#     top3.append(m)
#     top3_data = ','.join(top3)
# print(top3_data)

from functools import reduce

a = [10000,13000,14000,40000]

def fun(n):
    return n>10000
b = list(filter(fun, a))

def func(n):
    return n+(n*0.2)
c = list(map(func,b))

def func1(n,b):
    return n+b

d = reduce(func1,c)
print(c,d)