def solution(pl, ca):

    lst = [i for i in range(1,len(pl)+1)]
    dic = dict(zip(pl, lst))
    print(dic)

    for i in range(len(ca)):
        x = ca[i]
        if x in dic:
            y = dic[x]
            dic[x] = y-1
        if dic[1] == y-1:
            print(dic[0])
            print(dic[1])

''' 
실패
시간초과가 된다
니중에 다시 해보자
hashmap을 이용한 접근이 필요한 것 같다
'''