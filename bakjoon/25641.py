n = int(input())
str = input()
lst = []

for i in str:
    lst.append(i)

while True:
    if lst.count('t') == lst.count('s'):
        break
    else:
        lst.pop(0)

for i in lst:
    print(i,end='')