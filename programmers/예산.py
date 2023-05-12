import itertools

d = [1,3,2,5,4]
b = 9

# max=0
# lst=[]
# for i in range(1,len(d)+1):
#     ncr = list(itertools.combinations(d,i))
        
#     for j in ncr:
#         j = list(j)
#         print(j, sum(j))
#         if sum(j)<=b:
#             max = len(j)
#     answer = max

answer = 0
d.sort()
cnt=0
for i in d:
    if i <= b:
        cnt+=1
        b-=i
    else:break
answer = cnt
print(answer)
