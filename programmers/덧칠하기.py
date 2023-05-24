def solution(n, m, section):
    answer = 0
    lst = [i for i in range(1,n+1)]
    # print(lst)

    for i in range(len(lst)):
        if lst[i] in section:
            lst[i] = 0

    # print(lst)
    s1 = ''
    for i in lst:
        s1 += str(i)
    # print(s1)

    i = 0
    while len(s1):
        if s1[i] == '0':
            answer += 1
            i = i + m
            s1 = s1[i:]
            i = 0
        else:
            i += 1
            s1 = s1[i:]
            i = 0
        print(s1)
    # print(answer)
    return answer

'''
실패
어떤 사람은 덱으로 어떤 사람은 section 값 만큼만 비교해서 푸는 방법으로 풀었다
다시 한번 풀어야겠다
'''