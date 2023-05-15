from itertools import combinations

def solution(numbers):
    lst = []
    for i in combinations(numbers, 2):
        lst.append(i)
    print(lst)

    lst1 = []
    lst2 = []
    for i in lst:
        sum1 = 0
        lst1 = list(i)
        sum1 += sum(lst1)
        lst2.append(sum1)

    lst2 = set(lst2)
    lst2 = list(lst2)
    lst2.sort()
    print(lst2)

'''
처음에 정렬 후 set으로 바꾸고 다시 list로 바꾸는 식으로 했더니 계속 실패했다
그래서 정렬을 마지막에 했더니 성공했다
set은 순서가 없어서 정렬함수를 사용하지 못한다고 한다
그래서 틀린 것 같다
'''