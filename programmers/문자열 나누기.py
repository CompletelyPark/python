def solution(s):
    answer = 0
    cnt1 = 1
    cnt2 = 0

    lst = []
    for i in s:
        lst.append(i)

    s1 = lst[0]
    i = 1
    while i < len(lst):
        if lst[i] == s1:
            cnt1 += 1
        else:
            cnt2 += 1

        if cnt1 == cnt2:
            answer += 1

            # print(lst[:i+1])
            del lst[:i+1]
            if not len(lst) == 0:
                s1 = lst[0]
                # print(s1)
                cnt1 = 1
                cnt2 = 0
                i = 0

        # print(i, cnt1, cnt2)

        i += 1
    if not len(lst) == 0 and cnt1 > cnt2:
        answer += 1
    else:
        answer += len(lst)
    # print(answer)

    return answer

'''
사실 얼떨결에 된거라 코드 설명이 잘 안될 것 같다
33줄의 if문은 문자열 처리 후 문자가 남았는데 한 문자가 다른 문자들의 수보다
많다면 +1개로 처리한것이다
abaa의 경우 ab를 처리하고 aa만 남는데 이 같은 경우를 처리하려고 짠 것이다
abaaacb 같은 경우도 마찬가지다
else의 경우에는 이제보니 적용될일 이 많지는 않은 것 같다
'''