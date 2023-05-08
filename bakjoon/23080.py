n = int(input())
str = input()
str1 = ''
for i in range(0,len(str),n):
    str1 += str[i]
print(str1)