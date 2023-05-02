import itertools

num = int(input())

def func(num):
    for _ in range(num):
        sum=0
        sum1=0
        num1 = int(input())

        lst=[]
        for _ in range(num1):
            lst.append(list(map(int,input().split())))
        lst = list(itertools.chain.from_iterable(lst))

        k, d, a = map(int, input().split())

        for _ in range(num1):
            sum = k*lst.pop(0) - d*lst.pop(0) + a*lst.pop(0)
            if sum>0: sum1 += sum

        print(sum1)

func(num)