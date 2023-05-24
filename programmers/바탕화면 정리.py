def solution(wallpaper):
    answer = []
    x1 = 0
    x2 = 50
    y1 = 0
    y2 = 50
    lst2 = []
    for i in wallpaper:
        lst3 = []
        for j in i:
            lst3.append(j)
        lst2.append(lst3)


    cnt = 0
    for i in range(len(lst2)):
        if cnt == 0:
            if '#' in lst2[i]:
                x1 = i
                cnt += 1
    cnt = 0

    for i in range(len(lst2)-1, 0-1, -1):
        if cnt == 0:
            if '#' in lst2[i]:
                x2 = i
                cnt += 1
    # lst2 = list(zip(*lst2[::-1]))

    n = len(lst2)
    m = len(lst2[0])

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = lst2[i][j]

    # print(result)
    cnt = 0
    for i in range(len(result)):
        if cnt == 0:
            if '#' in result[i]:
                y1 = i
                cnt += 1


    cnt = 0
    for i in range(len(result) - 1, 0-1, -1):
        if cnt == 0:
            if '#' in result[i]:
                # print(i)
                y2 = i
                cnt += 1


    answer = [x1,y1,x2+1,y2+1]
    # print(answer)
    return answer

'''
실제 풀이 시간은 1시간 반정도 걸린 것 같다
생각보다 어려웠다 공부가 더 필요하다

n = len(lst2)
m = len(lst2[0])

result = [[0] * n for _ in range(m)]

for i in range(n):
    for j in range(m):
        result[j][n - i - 1] = lst2[i][j]

이 코드를 통해 뒤집어서 판별에 성공했다 
'''