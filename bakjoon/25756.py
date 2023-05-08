n = int(input())
# 1 - (1 - 현재 방무)(1 - 새로 들어온 방무 물약)
lst = list(map(int,input().split()))
v = 0
lst2 = []

for i in lst:
    ans = 1 - (1 - v) * (1 - i/100)
    v = ans
    ans *= 100
    ans = round(ans,6)
    lst2.append(ans)

for i in lst2:
    print(i)