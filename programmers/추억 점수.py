def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(na, ye))
    # print(dic)
    for i in ph:
        sum1 = 0
        for j in i:
            if j in dic:
                sum1 += dic[j]
        answer.append(sum1)
    # print(answer)
    return answer

'''
어려움 없었다
10분도 안걸린 것 같다
딕셔너리가 생각보다 너무 좋다
'''