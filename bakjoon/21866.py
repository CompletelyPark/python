lst1 = list(map(int, input().split()))
lst2 = [100,100,200,200,300,300,400,400,500]
cnt = 0
sum = 0
n = len(lst2)

for i in range(n):
    if lst1[i] > lst2[i]: cnt+=1
    sum+=lst1[i]

if cnt>=1: print('hacker')
elif sum>=100: print('draw')
else: print('none')