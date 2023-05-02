n = int(input())
max = 0
ans = 0
for _ in range(n):
    a,d,g=map(int,input().split())
    a1 = d+g
    if a==a1:
        ans = (d+g)*a*2
    else:
        ans = (d+g)*a

    if ans>=max:
        max = ans

print(max)    

