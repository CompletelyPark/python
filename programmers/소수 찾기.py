n = 5
ans=0
# for i in range(2,n+1):
#     cnt=0
#     for j in range(1,n+1):
#         if i%j==0:
#             cnt+=1
#     if cnt<=2:
#         ans+=1
lst=[False, False] + [True] * (n-1)
answer=[]
for i in range(2,n+1):
    if lst[i]:
        answer.append(i)
    for j in range(2*i, n+1,i):
        lst[j] = False

print(len(answer))