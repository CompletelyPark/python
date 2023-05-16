def solution(id_list, report, k):
    lst7 = tuple(id_list)
    id_list1 = id_list
    # print(id_list1, id_list)
    answer = []
    s1 = ''
    for i in report:
        s1 += i
        s1 += '/'
    s1 = s1.replace(' ', '-')

    lst = []
    x = 0
    j = 0
    for i in range(len(s1)):
        if s1[i] == '/':
            lst.append(s1[x:j])
            x = j + 1
        j += 1

    lst = set(lst)
    lst = list(lst)
    lst.sort()

    lst1 = []
    lst2 = []
    for i in range(len(lst)):
        x = lst[i].find('-')
        lst1.append(lst[i][:x])
        lst2.append(lst[i][x+1:])

    # lst1이 신고한 유저
    # lst2가 신고받은 유저

    id_list1.sort()
    lst4 = []
    lst5 = []
    y = 0
    y1 = 0
    for i in range(len(id_list1)):
        x = lst1.count(id_list1[i])
        x1 = lst2.count(id_list1[i])
        x = y + x
        x1 = y1 + x1
        lst5.append(lst1[y1:x1])
        lst4.append(lst2[y:x])
        y = x
        y1 = x1


    lst3 = [0 for _ in range(len(id_list1))]
    dic1 = dict(zip(id_list1, lst4)) # 각 유저가 신고한 딕셔너리
    dic2 = dict(zip(id_list1, lst5)) # 유저에게 신고 받은 딕셔너리
    # print('dic1', dic1)
    # print('dic2', dic2)
    dic3 = dict(zip(id_list1, lst3)) # k번 이상 신고 받았을 시 정지 받는 목록
    dic4 = dict(zip(id_list1, lst3)) # k번 이상 신고 받았을 시 정지 받는 목록

    for key, values in dic2.items():
        x = len(values)
        if x >= k:
            dic3.update({key: 1})

    # print('dic3', dic3)
    # print('dic4', dic4)
    for key, values in dic1.items():
        x = 0
        for i in values:
            if dic3[i] == 1:
                x += 1
                dic4.update({key: x})

    # print(dic4)

    lst7 = list(lst7)
    # print(lst7)
    # print(len(dic4))
    for i in lst7:
        if i in dic4:
            answer.append(dic4[i])
    # print(answer)
    return answer