def solution(survey, choices):
    answer = ''
    length = len(survey)
    lst = []
    for i in range(length):
        s = survey[i]
        x = choices[i] - 4
        if x > 0:
            s1 = s[1] + str(x)
            # print(s1)
            lst.append(s1)
        elif x < 0:
            s1 = s[0] + str(-1 * x)
            lst.append(s1)

    # print(lst)

    lst1 = [0 for _ in range(8)]
    lst2 = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    dic = dict(zip(lst2, lst1))
    # print(dic)

    for i in lst:
        if i[0] in dic:
            dic[i[0]] += int(i[1])
    # print(dic)

    for i in range(0, len(dic), 2):
        if dic.get(lst2[i]) >= dic.get(lst2[i+1]):
            # print(lst2[i])
            answer += lst2[i]
        else:
            # print(lst2[i+1])
            answer += lst2[i+1]

    # print(answer)
    return answer