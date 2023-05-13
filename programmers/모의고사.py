answers = [1,3,2,4,2]

x=1
lst1=[]
for i in range(len(answers)):
    lst1.append(x)
    x+=1
    if x>5:
        x=1

y=2
yx=1
lst2=[]
for i in range(len(answers)):
    if yx>5:
        yx=1

    if i%2!=0:
        lst2.append(yx)
    else:
        lst2.append(y)

    if i%2!=0 and yx==1:
        yx+=2
    elif i%2!=0:
        yx+=1 

print(lst2)
cnt=0
zx = 1
lst3=[3,3]
for i in range(2,len(answers)):
    lst3.append(zx)
    cnt+=1

    if cnt==2:
        cnt=0
        zx+=1
    if zx>5:
        zx=1

lstx=[]
cnt1=0
cnt2=0
cnt3=0
for i in range(len(answers)):
    if answers[i]==lst1[i]:
        cnt1+=1
    if answers[i]==lst2[i]:
        cnt2+=1
    if answers[i]==lst3[i]:
        cnt3+=1

lstx.append(cnt1)
lstx.append(cnt2)
lstx.append(cnt3)

m = max(lstx)

ans = []
if m==lstx[0]==lstx[1]==lstx[2]:
    ans=[1,2,3]
elif m==lstx[0]:
    ans.append(1)
elif m==lstx[1]:
    ans.append(2)
elif m==lstx[2]:
    ans.append(3)

print(ans)


    


