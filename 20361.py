# https://www.acmicpc.net/problem/20361

n, x, k = map(int,input().split())

ans = x
for i in range(k):
    a, b = map(int,input().split())
    if a == ans: 
        ans = b
        # print('a ',ans)
    elif b == ans: 
        ans = a
        # print('b', ans)

print(ans)