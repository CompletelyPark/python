def func(num):
    cnt = 0
    for x in range(num):
        x = input()
        x1 = x[2:]
        x1 = int(x1)
        if x1<=90:
            cnt+=1
    return cnt

num = input()
num = int(num)
print(func(num))