n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
answer=[]
for i in range(n):
    a = arr1[i]
    b = arr2[i]
    s = bin(a | b)
    s=s[2:]
    s= str(s)
    lst = []
    for i in s:
        lst.append(i)

    print(s)
    if a<2**n or b<2**n:
        for i in range(n-len(s)):
            lst.insert(i,'0')
    print(lst)

    s1=''
    for i in lst:
        if i=='1':
            s1+='#'
        else:
            s1+=' '
    answer.append(s1)
print(answer)