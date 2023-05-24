def solution(cards1, cards2, goal):
    answer = ''

    cards1.reverse()
    cards2.reverse()
    # print(goal,cards1,cards2)
    i = 0
    while len(goal):
        if len(cards1) != 0 and goal[i] == cards1[len(cards1)-1]:
            cards1.pop()
            goal.remove(goal[i])
        elif len(cards2) != 0 and goal[i] == cards2[len(cards2)-1]:
            cards2.pop()
            goal.remove(goal[i])
        else:
            break

    if len(goal) == 0:
        answer = 'Yes'
    else:
        answer = 'No'
    # print(answer)

    return answer

'''
처음에 로직은 맞게 구성했다
reverse를 한 이유는 remove를 쓰지 않고 pop을 쓰기 위해서 reverse를 했다
그리고 goal의 각 위치에 맞는 요소가 cards1 이나 cards2에 있으면
각각 제거해서 확인한다
len(cards1)을 준 이유는 먼저 각 카드의 요소가 제거 되면서 카드가 0 이 되면
거기선 검색을 하지 않기 위해 줬다
goal에 요소가 남아있으면 틀린 것을 판결했다. 
'''