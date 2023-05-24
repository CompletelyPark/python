def solution(s, skip, index):
    answer = ''
    lst = []
    for i in skip:
        lst.append(i)

    for i in s:
        lst2 = []
        x = ord(i)

        while len(lst2) < index:
            if chr(x) == 'z':
                x = 96
            x += 1
            print(chr(x), end= ' ')
            if chr(x) not in lst:

                lst2.append(chr(x))
            if chr(x) == 'z':
                x = 96

        print(lst2)
        answer += lst2[index-1]
    print(answer)
    return answer
'''
문자열로 z가 오고 index로 1이 오는 경우에 문제가 발생했다
처음에는 z를 a로 돌릴생각만 해서 a = 97로 줬더니 그 다음에 인식이 b부터 돼서 a = 96으로 줬다
뒤에서만 z를 판별했더니 입력으로 z가 오는 경우에 문제가 발생했다
그래서 z 판별을 앞 뒤로 줬다
'''