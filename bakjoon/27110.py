num = int(input())
lst=list(map(int,input().split()))


def func(num,lst):
    sum=0
    for x in lst:
        y= x-num
        if y<0:
            sum+=x
        else:
            sum+=num
    return sum

print(func(num,lst))