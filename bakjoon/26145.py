n,m = map(int, input().split())
lst=list(map(int,input().split()))

lst2=[]
lst3=[]

for i in range(n):
    lst1=list(map(int,input().split()))
    lst2.append(lst1)

for i in range(n):
    s1 = sum(lst2[i])
    lst[i] -= s1
    for j in range(n+m):
        lst3[j] = lst3[j]+lst2[i][j]
        
for i in range(n):
    lst3[i] = lst[i] + lst3[i]

print(*lst3)