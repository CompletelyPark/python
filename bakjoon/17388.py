# https://www.acmicpc.net/problem/17388
from sys import stdin

s, k, h = map(int,stdin.readline().split())
min1 = min(s,k,h)

if s+k+h>=100:
    print('OK')

elif s+k+h<100:
    if min1 == s:
        print('Soonsil')
    elif min1 == k:
        print('Korea')
    else:
        print('Hanyang')
