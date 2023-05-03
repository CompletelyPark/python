# https://www.acmicpc.net/problem/27736

n = int(input())
lst = list(map(int, input().split()))

c1 = lst.count(1)   # 찬성
c2 = lst.count(0)   # 기권
c3 = lst.count(-1)  # 반대

if c2 >= n/2:
    print('INVALID')
else:
    if c1>c3:
        print('APPROVED')
    else:
        print('REJECTED')

