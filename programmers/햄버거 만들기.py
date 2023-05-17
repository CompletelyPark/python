def solution(ilst):
    s1 = ''
    cnt = 0
    for i in range(len(ilst)):
        s1 += str(ilst[i])
        print('밖', s1)
        if '1231' in s1:
            # print(i)
            cnt += 1
            # print(s1[:i-3])

            s1 = s1[:len(s1)-4]

    print(cnt)
    return cnt

'''
실패
시간복잡도가 항상 문제다
다른 풀이방법을 봤더니 인덱스와 del 을 이용해서 풀었다
리스트에서 인덱스를 통해 바로 검색해서 그자리에서 삭제후 다시 검색하는 방식으로
진행한 것 같다
for문에서 재할당이 시간을 많이 잡아먹는다고 한다
replace도 오래 걸린다고 한다
시간 복잡도 너무 어렵다
'''