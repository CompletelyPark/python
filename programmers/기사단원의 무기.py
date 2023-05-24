def solution(number, limit, power):
    answer = 0
    if limit == 1:
        answer += power
    else: answer += 1
    for i in range(2, number+1):
        # print('i ', i)
        cnt = 0
        for j in range(1, int(i **(1/2)) +1):
            if i % j == 0:
                # print('j ', j)
                cnt += 2
                if i/j == j:
                    cnt -=1

        # print(cnt)
        if cnt > limit:
            answer += power
        else:
            answer += cnt

    # print(answer)
    return answer

'''
처음에 생각은 1부터 numbers까지 모두 검색하면 분명 시간복잡도에 걸릴테니까 생각하고
구글링을 했다
처음에는 int(i **(1/2)) +1 이렇게 했다가 약수 갯수가 틀리게 나와서
n // 2 + 1 이렇게 했더니 정답은 맞게 나왔다
하지만 시간 복잡도에서 걸렸다
절반만 반복하는 방법과 약수를 구하려는 수의 제곱근만큼만 반복하는 방법이 있었다
24의 경우 절반은 12번이지만 제곱근의 경우는 약 4.9배로 2.5배 향상이 됐다
int를 취했을 때 반올림 되는 것 같다
'''