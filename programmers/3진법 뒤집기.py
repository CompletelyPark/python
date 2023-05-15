def solution(n):
    lst = []
    while n > 0:
        x = n % 3
        lst.append(x)
        n //= 3

    sum = 0
    y = len(lst) - 1
    for i in range(len(lst)):
        sum += lst[i]*(3**y)
        y -= 1

    return sum