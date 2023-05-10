s = "Pyy"
pcnt=0
ycnt=0
for i in s:
    if i=='p' or i=='P':
        pcnt+=1
    elif i=='y' or i=='Y':
        ycnt+=1

if pcnt==ycnt:
    print('true')
else:
    print('false')