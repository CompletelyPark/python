# https://www.acmicpc.net/problem/17945
from sys import stdin
import math

a, b = map(int,stdin.readline().split())

# x2 + 2ax + b = 0 
x = (a * -2 + math.sqrt((2*a)**2-4*1*b)) / 2
y = (a * -2 - math.sqrt((2*a)**2-4*1*b)) / 2
x = int(x)
y= int(y)

if x==y:
    print(x)
else:
    print(min(x,y), max(x,y))