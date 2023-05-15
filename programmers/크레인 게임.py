# 실패

def solution(board, moves):
    answer = 0

    lst1 = list(zip(*board))
    lst2 = []
    for i in lst1:
        i=list(i)
        lst2.append(i)
        print(type(lst2))
    print(lst2)

    x = len(board)
    lst = []
    z = 0

    for i in moves:
        for j in lst2[i-1]:
            if j != 0:
                z = lst2[i-1].index(j)
                lst2[i-1][z] = 0
                lst.append(j)

                if len(lst) > 1:
                    if lst[-1] == lst[-2]:
                        lst.pop(-1)
                        lst.pop(-1)
                        answer += 2
                break
    return answer