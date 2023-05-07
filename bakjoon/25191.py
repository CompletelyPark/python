n = int(input())
x, y = map(int,input().split())

x1 = x//2
y1 = y
if x1+y1<=n:
    print(x1+y1)
else:
    print(n)