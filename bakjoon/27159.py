num = int(input())
lst=list(map(int,input().split()[:num]))
lst.append(0)

def func(num,lst):
    lst2=[]
    lst3=[]
    sum=0
    for i in range(num):
        lst2.append(lst[i])
        if lst[i+1]-lst[i]!=1:
            lst3.append(lst2[0])
            lst2=[]

    for j in lst3:
        sum+=j

    print(sum)

func(num,lst)