def solution(today, terms, privacies):
    answer = []

    lst1 = []
    lst2 = []
    for i in range(len(terms)):
        x = terms[i].index(' ')
        lst1.append(terms[i][:x])
        lst2.append(int(terms[i][x+1:]))
    dic = dict(zip(lst1, lst2))
    # print(dic)

    today_year = int(today[:4])
    today_month = int(today[5:7])
    today_day = int(today[8:])
    # print(today_year, today_month, today_day)

    for i in range(len(privacies)):
        x = privacies[i].index(' ')
        privacies_year = int(privacies[i][:4])
        privacies_month = int(privacies[i][5:7])
        privacies_day = int(privacies[i][8:10])
        y = 0
        if privacies[i][x+1:] in dic.keys():
            y = dic[privacies[i][x+1:]]

        privacies_month += y
        # print(privacies_month)

        if privacies_month % 12 == 0 and privacies_month // 12 > 1:
            privacies_year += (privacies_month // 12) - 1
            privacies_month = 12

        elif privacies_month > 12:
            privacies_year += privacies_month // 12
            privacies_month = privacies_month % 12


        print(privacies_year,privacies_month,privacies_day)

        if today_year > privacies_year:
            answer.append(i+1)
        elif today_year == privacies_year:
            if today_month > privacies_month:
                answer.append(i+1)
            elif today_month == privacies_month:
                if today_day >= privacies_day:
                    answer.append(i+1)

    # print(answer)
    return answer

'''
privacy month가 12가 넘어가는 경우에 문제가 발생했다
12일 때는 월이 0으로 나왔고
month가 24 36 이럴 경우에는 1년 2년 추가임에도 
privacies_year += privacies_month // 12 이였기 때문에
2년 3년 추가를 해서 틀렸다
그래서 12로 나눈 나머지가 0일때 그리고 month가 12보다 클때 추가적인 조건을 줘서 해결했다
먼저 나머지가 0일경우 
privacies_year += (privacies_month // 12) - 1 해서 
month가 24일 경우를 예로 들면 1년 추가이기 때문에 2 - 1 을 해주는 방식으로 했고
나머지가 0이기 때문에 month는 12로 맞춰줬다

처음에는 시간문제에 걸릴것 같았는데 오히려 다른 부분에서 틀린 문제였다
다른 사람의 풀이를 보니 map과 enumerate를 써서 간단하게 푼 것 같다
enumerate를 공부해야겠다
'''