def solution(a, b, n):
    answer = 0
    sum = 0

    while n >= a:
        x = n % a
        n = n // a
        n1 = n * b
        sum += x
        answer += n1
        # print(n,x,sum)
        n = n1 + x

    # print(answer)

    return answer

'''
틀림
1. 시간초과 
2. 문제 이해 부족

'''