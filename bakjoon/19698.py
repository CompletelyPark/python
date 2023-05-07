# https://www.acmicpc.net/problem/19698

n, w, h, l = map(int,input().split())

ans = (w//l) * (h//l)

if ans<=n:
    print(ans)
else:
    print(n)