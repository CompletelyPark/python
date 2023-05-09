# https://www.acmicpc.net/problem/17450
from sys import stdin

s1, s2 = map(float,stdin.readline().split())
n1, n2 = map(float,stdin.readline().split())
u1, u2 = map(float,stdin.readline().split())

s = s2/s1
n = n2/n1
u = u2/u1

if max(s,n,u)==s:
    print('S')
elif max(s,n,u)==n:
    print('N')
else:
    print('U')
