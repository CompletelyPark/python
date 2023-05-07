# https://www.acmicpc.net/problem/20053

t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    print(min(lst), max(lst))