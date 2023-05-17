import itertools

def solution(number):
    answer = 0
    cnt = 0
    for i in itertools.combinations(number,3):
        if sum(i) == 0:
            cnt += 1
    # print(cnt)
    return cnt