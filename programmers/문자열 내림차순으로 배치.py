s = "Zbcdefg"
lst=[]
lst1=[]
for i in s:
    # if i.isupper():
    #     lst1.append(i)
    # else:
    lst.append(i)
lst.sort(reverse=True)
# lst1.sort(reverse=True)


answer = ''
for i in lst:
    answer = answer + i

print(answer)