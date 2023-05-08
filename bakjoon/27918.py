# https://www.acmicpc.net/problem/27918

n =int(input())

d=0
p=0

for _ in range(n):
    x = input()

    if x=='D':
        d+=1
    else: p+=1
    
    fi = abs(d-p)
    if fi>=2:
        break

print('%d:%d'%(d,p))

# using for statement to input string
# if one side gets 2 points higher than the other side
# 2 points make a distinction absolute value easily
# break
