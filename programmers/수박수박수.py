
n = 3
lst=[]
ans=''
a = '수'
b = '박'
for i in range(n):
    if i%2!=0:
        ans+=b
    else:
        ans+=a

print(ans)