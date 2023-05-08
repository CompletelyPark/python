# https://www.acmicpc.net/problem/27960

sa, sb = map(int,input().split()) # input
lst1 = [1,1,1,1,1,1,1,1,1,1]      # grade list 1
lst2 = [1,1,1,1,1,1,1,1,1,1]      # grade list 2
lst3=[]                           # sa convert binary number list
lst4=[]                           # sb convert binary number list

# convert binary number 
while sa!=0:
    a = sa%2
    sa//=2
    lst3.append(a) 

while sb!=0:
    b = sb%2
    sb//=2
    lst4.append(b) 

# check grade list 
for i in range(len(lst3)):
    if lst1[i]==lst3[i]:
        lst1[i]=0

for i in range(len(lst4)):
    if lst2[i]==lst4[i]:
        lst2[i]=0

# c's check grade
n = 1
ans = 0
for i in range(10):
    if lst1[i]!=lst2[i]:
       ans+=n
    n*=2 

print(ans) 
 
