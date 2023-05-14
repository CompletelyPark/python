import operator

N=4
stages=[4,4,4,4,4]
lst=[]
int_lst=[]
stages.sort()
for i in range(1,N+1):
    x = stages.count(i)
    lst.append(x)


for i in range(1,N+1):
    int_lst.append(i)

lst1=[]    
z = len(stages)
for i in lst:
    if i==0:
        y=0
    else:
        y = i/z
    z-=i
    lst1.append(y)

dic1 = dict(zip(int_lst,lst1))
d1 = sorted(dic1.items(),key=operator.itemgetter(1),reverse=True)
lst2=[]
for i in d1:
    lst2.append(i[0])
print(lst2)    