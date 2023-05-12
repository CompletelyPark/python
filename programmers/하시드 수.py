x = 11
s = str(x)
a=0
for i in s:
    a += int(i)

if x%a==0:
    print(True)
else:
    print(False)