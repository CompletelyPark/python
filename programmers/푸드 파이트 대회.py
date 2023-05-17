def solution(ilst):
    s1 = ''
    s = 1
    for i in range(1, len(ilst)):
        for _ in range(ilst[i]//2):
            s1 += str(i)
    s2 = s1[::-1]
    # print(s2)
    s1 += '0'
    s1 += s2
    # print(s1)
    return s1

'''
이중 for문을 써서 음식이 많은 경우에는 시간초과가 나올 것 같다
이중 for문을 쓰지 않고 코딩하는 방식을 생각해봐야 할 것 같다
음
다른 사람 풀이 중에 enumerate가 있었는데 한번 확인해 봐야 겠다
'''