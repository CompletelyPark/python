# https://www.acmicpc.net/problem/17350

n = int(input())

x = 0
for _ in range(n):
    str = input()
    if str=='anj':
        x=1

if x==1:
    print('뭐야;')
else:
    print('뭐야?')
