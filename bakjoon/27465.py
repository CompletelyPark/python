# https://www.acmicpc.net/problem/27465 

n = int(input())
cnt = 0
ans = 0

while True:
    for i in range(1,n):
        if n%i==0:
            cnt+=1

    if cnt>1:
        ans = n
        break
    n+=1

print(ans)