# https://www.acmicpc.net/problem/18247
from sys import stdin

t = int(stdin.readline())
lst_ans = []
lst_ans_int = list(map(int,lst_ans))

for _ in range(t):
    n, m = map(int,stdin.readline().split())
    if n<12 or m<4:
        lst_ans_int.append(-1)
    else:
        x = 12 * m
        y = m-4
        lst_ans_int.append(x-y)

for i in lst_ans_int:
    print(i)
# L 열은 12번째