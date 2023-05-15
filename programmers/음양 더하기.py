def solution(a, b):
    answer = 123456789
    x = len(a)
    sum = 0
    for i in range(x):
        if not b[i]:
            sum += -1 * a[i]
        else:
            sum += a[i]
    answer = sum
    print(answer)
    return answer