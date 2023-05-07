# https://www.acmicpc.net/problem/21312

lst = list(map(int, input().split()))

a= lst[0]
b= lst[1]
c= lst[2]

ab = a*b
bc = b*c
ac = a*c
abc = a*b*c

lst1=[]
lst2=[]
lst3=[]
lst3.extend([a,b,c,ab,bc,ac,abc])

for i in lst3:
    if i%2 == 0:
        lst1.append(i)
    else:
        lst2.append(i)

if len(lst2)>=1:
    print(max(lst2))
else:
    print(max(lst1))