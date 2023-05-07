# https://www.acmicpc.net/problem/27890

x,n = map(int, input().split())

for _ in range(n):
    if x%2==0:
        x = x // 2
        x = x ^ 6 
    else:
        x = 2 * x
        x = x ^ 6

print(x)

# xor 연산은 " ^ " 로 계산이 가능하다