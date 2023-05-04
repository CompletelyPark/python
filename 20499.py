# https://www.acmicpc.net/problem/20499

str = input()
lst = []

for i in str:
    lst.append(i) 

lst[:] = (value for value in lst if value !='/')
lst_int = list(map(int,lst))

ans = ''
if len(lst_int)==3:
    if(lst_int[0]+lst_int[2]<lst_int[1] or lst_int[1]==0):
        ans = 'hasu'
    else: ans = 'gosu'
else:
    if(lst_int[0]*10+lst_int[1]+lst_int[3]<lst_int[2] or lst_int[2]==0):
        ans = 'hasu'
    else: ans = 'gosu'

print(ans)