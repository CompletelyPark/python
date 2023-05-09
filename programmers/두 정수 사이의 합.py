# https://school.programmers.co.kr/learn/courses/30/lessons/12912

a=3
b=5
ans = 0
c=0
    
if a>b:
    c=b
    b=a
    a=c

for i in range(a,b+1):
    ans+=i

print(ans)