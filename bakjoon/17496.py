# https://www.acmicpc.net/problem/17496
from sys import stdin

n,t,c,p = map(int,stdin.readline().split())

cnt=0
x = 0
for i in range (1,n+1,t):
    print(i)
    cnt+=1
    x = i

if x+t>n:
    cnt-=1

print(cnt*c*p)