def solution(park, routes):
    routes.reverse()
    lst = []

    for i in park:
        lst2 = []
        for j in i:
            lst2.append(j)
        lst.append(lst2)

    n = len(lst)
    m = len(lst[0])

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][i] = lst[i][j]

    sx = 0
    sy = 0
    length = 0
    for i in range(len(lst)):
        length = len(lst[i])
        if 'S' in lst[i]:
            sy = i
            sx = lst[i].index('S')
    # print(sy, sx)

    while len(routes):
        r = routes.pop()
        rx = r[0]
        ry = int(r[2])
        if rx == 'E' and sx + ry <= length - 1:
            if 'X' not in park[sy][sx:sx+ry+1]:
                sx += ry

        elif rx == 'W' and sx - ry >= 0:
            if 'X' not in park[sy][sx - ry:sx+1]:
                sx -= ry

        elif rx == 'S' and sy + ry <= len(result) - 1:
            if 'X' not in result[sx][sy:sy + ry + 1]:
                sy += ry

        elif rx == 'N' and sy - ry >= 0:
            if 'X' not in result[sx][sy - ry:sy + 1]:
                sy -= ry

    print(sy, sx)
    answer = [sy, sx]
    return answer

'''
문제를 잘 읽고 이해하는 능력을 키워야겠다고 생각했다
문제를 모두 푸는데는 딴짓도 해서 오래 걸렸지만
로직을 만드는 것은 생각보다 금방 했다
'''