def solution(sizes):
    answer = 0

    for i in range(len(sizes)):
        a = min(sizes[i][0], sizes[i][1])
        b = max(sizes[i][0], sizes[i][1])
        sizes[i][0] = a
        sizes[i][1] = b

    m1 = sizes[0][0]
    m2 = sizes[0][1]
    for i in range(1, len(sizes)):
        if m1 <= sizes[i][0]:
            m1 = sizes[i][0]
        if m2 <= sizes[i][1]:
            m2 = sizes[i][1]

    return m1 * m2
