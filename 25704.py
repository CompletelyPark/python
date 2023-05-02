n = int(input())
p = int(input())
lst = [0]

if n>=5:
    lst.append(500)
if n>=10:
    lst.append(p//10)
if n>=15:
    lst.append(2000)
if n>=20:
    lst.append(p//4)

p = p - max(lst)
if p< 0:
    p = 0
print(p)