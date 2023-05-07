n = int(input())
str = input()
n1 = n-1
cnt = 0
lst = []

for i in str:
    lst.append(i)

for i in range(n//2):
    if lst[i] == lst[n1]:
        n1-=1
        continue
    else:
        n1-=1
        cnt+=1

print(cnt)