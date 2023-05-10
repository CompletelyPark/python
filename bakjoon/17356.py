# https://www.acmicpc.net/problem/17356
from sys import stdin

x, y = map(float,stdin.readline().split())

a = (y-x)/400
ans = 1/(1+10**a)
print(ans)