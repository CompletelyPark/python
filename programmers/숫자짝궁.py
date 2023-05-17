def solution(x, y):
    answer = ''

    lst1 = []
    lst2 = []
    for i in str(x):
        lst1.append(i)
    for i in str(y):
        lst2.append(i)

    lst3 = []
    for i in lst1:
        # if i in lst2:
        #     lst3.append(int(i))
        #     lst2.remove(i)

    # print(lst3)
    #
    # if len(lst3) == 0:
    #     answer = '-1'
    #
    # s1 = ''
    # while len(lst3) > 0:
    #     s1 += str(max(lst3))
    #     lst3.remove(max(lst3))
    #
    # print(int(s1))
    # answer = str(int(s1))
    #
    # print(answer)
    return answer

'''
실패
시간복잡도에서 걸린다

'''