s= "1234"

lst=[]
lst1=['0','1','2','3','4','5','6','7','8','9']
for i in s:
    lst.append(i)

x = 0
if len(lst)==4 or len(lst)==6:
    for i in lst:
        if i not in lst1:
            x=1
else:
    x=1

if x==1:
    print('false')
else:
    print('true')