# https://school.programmers.co.kr/learn/courses/30/lessons/12906

lst = [1,1,3,3,0,1,1]
lst1 = []
lst1.append(lst[0])

a = lst[0]
for i in range(1,len(lst)):
    if lst[i]==a:
        a = lst[i]
        continue
    else:
        a = lst[i]
        lst1.append(lst[i])

print(lst1)
