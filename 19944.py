# https://www.acmicpc.net/problem/19944

n, m = map(int,input().split())

if n == m:
    print('OLDBIE!')
elif n > m:
    print('NEWBIE!')
else:
    print('TLE!')