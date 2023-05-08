# https://www.acmicpc.net/problem/18883
from sys import stdin

n, m = map(int,stdin.readline().split())

lst = list(i for i in range(1, n*m+1))

for i in lst:
    if i%m==0:
        print(i,end='')
        print('')
    else:
        print(i,end=' ')
        