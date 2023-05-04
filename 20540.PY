# https://www.acmicpc.net/problem/20540

lst = []

str = input()
for i in str:
    lst.append(i)

EI = lst[0] 
SN = lst[1]
TF = lst[2]
JP = lst[3]

ans =''

if EI=='E':
    ans = ans + 'I'    
else: ans = ans + 'E' 

if SN=='S':
    ans = ans + 'N' 
else: ans = ans + 'S' 

if TF=='T':
    ans = ans + 'F' 
else: ans = ans + 'T' 

if JP=='J':
    ans = ans + 'P' 
else: ans = ans + 'J' 

print(ans)
