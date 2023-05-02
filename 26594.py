str = input()
lst=[]
lst2 = ['Z','O','A','C']
lst3 = [0,0,0,0]
for i in str:
    lst.append(i)
num = len(str)

for i in range(num):
    for j in range(4):
        if lst2[j]==lst[i]:
            lst3[j]+=1

print(min(lst3))