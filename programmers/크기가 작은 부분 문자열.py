def solution(t, p):
    answer = 0

    length = len(p)
    lst = []

    for i in range(len(t)):
        lst.append(int(t[i:length+i]))
        if i == len(t)-length:
            break
    # print(lst)

    for i in lst:
        if int(p) >= int(i):
            answer += 1

    # print(answer)
    return answer

'''
처음에 문제를 잘못 이해해서 숫자로 들어오는 줄 알았다
계속 typeerror 가 나길래 뭔지 해서 문제를 다시 봤더니
t랑 p가 문자열로 들어오길래 수정해서 제출했더니 맞췄다
추가로 break를 준 이유는 인덱스 범위 초과가 일어날까봐 넣었다
'''