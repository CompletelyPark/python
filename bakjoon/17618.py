# https://www.acmicpc.net/problem/17618
from sys import stdin

n = int(input())
cnt = 0
x = 0

for i in range(1,n+1):
    x = i
    sum = 0
    while True:
        a = x%10
        sum+=a
        x = x//10
        if x==0:
            break
    if i%sum==0:
        cnt+=1

print(cnt)

# 78점
