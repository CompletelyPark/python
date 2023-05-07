from sys import stdin

n, k = map(int,stdin.readline().split())
k1 = k%10
k2 = k*2%10
lst = []

for i in range(1,n+1):
    lst.append(i)

for i in range(1,n+1):
    j = i%10
    if j==k1 or j==k2:
        lst.remove(i)

print(len(lst))
for i in lst:
    print(i,end=' ')