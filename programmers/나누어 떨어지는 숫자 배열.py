# https://school.programmers.co.kr/learn/courses/30/lessons/12910

arr = [5,9,7,10]
d = 5
lst = []
for i in arr:
    if i%d==0:
        lst.append(i)
lst.sort()
print(lst)