# https://school.programmers.co.kr/learn/courses/30/lessons/12901

lst2 = ['FRI','SAT','SUN','MON','TUE','WED','THU']
lst3 = [1,3,5,7,8,10,12]
lst4 = [4,6,9,11]
lst6 = []
z = 0

for i in range(1,12+1):
    lst5 = []

    if i in lst3:
        for _ in range(1,31+1):
            lst5.append(z)
            z+=1
            if z>6:
                z=0

    elif i in lst4:
        for _ in range(1,30+1):
            lst5.append(z)
            z+=1
            if z>6:
                z=0
    else: 
        for _ in range(1,29+1):
            lst5.append(z)
            z+=1
            if z>6:
                z=0

    lst6.append(lst5)

a = 5
b = 24

ans = lst6[a-1][b-1]
print(lst2[ans])