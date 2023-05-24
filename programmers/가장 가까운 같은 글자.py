def solution(s):
    answer = []
    lst = []
    for i in range(len(s)):
        if s[i] not in lst:
            lst.append(s[i])
            answer.append(-1)
        else:
            lst.reverse()
            answer.append(lst.index(s[i])+1)
            lst.reverse()
            lst.append(s[i])

    # print(lst)
    # print(answer)
    return answer

'''
먼저 알파벳이 새로운 리스트 안에 없다면 answer에 -1을 넣고
그다음에 lst에도 집어넣는다
만약 알파벳이 새로운 리스트 안에 있다면
lst를 뒤집어서 해당 알파벳의 인덱스를 갖고온다
왜 뒤집어서 갖고오냐면 index는 가장 맨처음에 만나는 요소를 갖고 오기 때문에 reverse를 해준다면
가장 가까운 순서대로 검색이 가능하기 때문이다
이때 +1을 하는 이유는 인덱스는 0번부터 시작하기 때문에 +1을 해줘서 몇 칸 차이가 나는지를 표시하기 위함이다.
'''