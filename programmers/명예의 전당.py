def solution(k, score):
    answer = []
    lst = []
    for i in score:
        lst.append(i)
        lst.sort()
        # print(lst)
        if len(lst) > k:
            del lst[0]
        answer.append(min(lst))
    # print(answer)
    return answer

'''
정렬 안하고 remove(min(lst))해서 하는 방법이 있는데
만약 똑같은 값이 들어오면 remove는 
remove는 무조건 처음 만나는 요소만 지우니까 상관이 없다
정렬을 굳이 하지 않고 해도 될 것 같다
'''