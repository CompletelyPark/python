def solution(k, m, score):
    answer = 0

    score.sort()
    # print(score)

    while m <= len(score):
        answer += min(score[:-m-1:-1]) * m
        del (score[:-m-1:-1])
    # print(answer)
    return answer

'''
어제 햄버거 문제에서의 다른 사람의 풀이를 응용해봤다
다른 사람이 푼 코드는 1줄짜리가 있었는데 [len(score)%m::m]에서 
len(score)%m 이부분이 약간 이해가 되지 않아서 손으로 풀어봐야 할 것 같다
왜 나머지를 주냐면 정렬후에 큰 숫자부터 빼간다고 했을때 어차피 제일 작은 수들은
남기 때문에 저렇게 코드를 짜도 가능한 것 같다
'''