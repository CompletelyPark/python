# https://school.programmers.co.kr/learn/courses/30/lessons/12903

str = input()
lst = []

for i in str:
    lst.append(i)
answer = ''

if len(lst)%2==1:
    answer = lst[len(lst)//2]
    print(answer)
else:
    answer = lst[len(lst)//2-1] + lst[len(lst)//2]
    print(answer)