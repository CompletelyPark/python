# 실패

def solution(numbers, hand):
    # numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]

    answer = ''
    answer_lst = []
    lefts = [1, 4, 7]
    rights = [3, 6, 9]
    middles = [2, 5, 8, 0]
    lefts_lst = []
    rights_lst = []
    middles_lst = []

    for i in numbers:
        if i in lefts:
            lefts_lst.append(lefts.index(i) + 1)
            rights_lst.append(-1)
            middles_lst.append(-1)
            answer_lst.append('L')

        elif i in rights:
            lefts_lst.append(-1)
            rights_lst.append(rights.index(i) + 1)
            middles_lst.append(-1)
            answer_lst.append('R')

        else:
            lefts_lst.append(-1)
            rights_lst.append(-1)
            middles_lst.append(middles.index(i) + 1)
            answer_lst.append('M')

    for i in range(len(numbers)):

        if lefts_lst[i] == 1:
            lefts_lst[i] = 3
        elif lefts_lst[i] == 3:
            lefts_lst[i] = 1

        if rights_lst[i] == 1:
            rights_lst[i] = 3
        elif rights_lst[i] == 3:
            rights_lst[i] = 1

        if middles_lst[i] == 3:
            middles_lst[i] = 1
        elif middles_lst[i] == 1:
            middles_lst[i] = 3
        elif middles_lst[i] == 4:
            middles_lst[i] = 0

    print(lefts_lst)
    print(rights_lst)
    print(middles_lst)

    x = -1
    y = -1
    j = 0
    lm = False
    lr = False

    for i in numbers:
        print(i, end='   ')
        z1 = abs(middles_lst[j] - x)
        z2 = abs(middles_lst[j] - y)
        print(z1, z2, end='   ')

        if i in lefts:
            x = lefts_lst[j]
            lm = False
            print(lm, end='   ')
            print(lr, end='   ')

        elif i in rights:
            y = rights_lst[j]
            lr = False
            print(lm, end='   ')
            print(lr, end='   ')

        else:
            z3 = abs(z1 - z2)
            print(z3, end='   ')
            if z3 == 0:
                if hand == 'left':
                    answer_lst[j] = 'L'
                    x = middles_lst[j]
                    lm = True
                else:
                    answer_lst[j] = 'R'
                    y = middles_lst[j]
                    lr = True

            elif z3 == 1:

                if hand == 'left' and lm:
                    answer_lst[j] = 'L'
                    x = middles_lst[j]
                    lm = True

                elif hand == 'right' and lr:
                    answer_lst[j] = 'R'
                    y = middles_lst[j]
                    lr = True

            else:
                if z1 < z2:
                    answer_lst[j] = 'L'
                    x = middles_lst[j]
                    lm = True

                elif z1 > z2:
                    answer_lst[j] = 'R'
                    y = middles_lst[j]
                    lr = True
        j += 1
        print('')
    print(answer_lst)

    return answer