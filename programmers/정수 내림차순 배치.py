n = 118372
lst=[]
for i in str(n):
    lst.append(i)
lst.sort(reverse=True)
s=''
for i in lst:
    s+=i
answer = int(s)
print(answer)