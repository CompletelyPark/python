# https://www.acmicpc.net/problem/18856
from sys import stdin

n = int(stdin.readline())

lst = [1,2,]
i = 3
for _ in range(n-len(lst)-1):
    lst.append(i)
    i+=1

while True:
    cnt = 0
    for j in range(1,i):
        if i%j==0:
            cnt+=1
    if cnt>1:
        i+=1
    else: break

lst.append(i)

for x in lst:
    if x!= i:
        print(x,end=' ')
    else:
        print(x,end='')