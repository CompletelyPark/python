x, y = map(int, input().split())

x1 = x//2
if x==1:
    print('0')
else:
    if x1<=y:
        print(x1)
    else:
        print(y)
