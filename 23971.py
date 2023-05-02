from sys import stdin

lst = list(map(int, stdin.readline().split()))
h = lst[0]
w = lst[1]
n = lst[2]
m = lst[3]


cnt = 0

for i in range(0,h,n+1):
    for j in range(0,w,m+1):
        cnt+=1
        
print(cnt)

