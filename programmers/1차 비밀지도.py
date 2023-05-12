n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
answer=[]

for i in range(n):
    a = arr1[i]
    b = arr2[i]
    x = format(a,'b')
    x = str(x)
    y = format(b,'b')
    y = str(y)

    print(x,y)
    
    lst1=[]
    for i in x:
        lst1.append(i)
    lst1.reverse()

    lst2=[]
    for i in y:
        lst2.append(i)
    lst2.reverse()

    if n!=len(lst1) and n!=len(lst2):
        for i in range(n-len(lst1)):
            lst1.append('0')
        for i in range(n-len(lst2)):
            lst2.append('0')

    elif n!=len(lst1):
        for i in range(n-len(lst1)):
            lst2.append('0')

    else:
        for i in range(n-len(lst2)):
            lst2.append('0')

    print(lst1)
    print(lst2)

    lst3=[]
    for i in range(n):
        if lst1[i]=='1'or lst2[i]=='1':
            lst3.append('#')
        else:
            lst3.append(' ')
    lst3.reverse()
    print(lst3)
    
    str1 = ''
    for i in lst3:
        str1+=i
        
    answer.append(str1)
print(answer)


