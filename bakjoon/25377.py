n = int(input())
min = 1000
cnt = 0
ans = 0
for _ in range(n):
    x,y = map(int,input().split())
    if y>=x:
        if min>y:
            min = y
    else:
        cnt+=1

    if cnt!=n:
        ans = min
    else:
        ans = -1 
print(ans)