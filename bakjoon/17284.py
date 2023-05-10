# https://www.acmicpc.net/problem/17284

lst1 = list(map(int,input().split())) 

ans = 5000
for i in lst1:
    if i==1:
        ans-=500
    elif i==2:
        ans-=800
    else:
        ans-=1000

print(ans)
