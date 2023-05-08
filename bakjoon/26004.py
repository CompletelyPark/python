num = int(input())
str = input()

def func(num, str):
    lst = ['H','I','A','R','C'] # 알파벳 검증을 위한 리스트
    lst2=[0,0,0,0,0] # 각 알파벳의 개수 리스트
    lst3 = [] # 입력된 문자열을 리스트로 바꾸기 위한 빈 리스트

    for i in str:
        lst3.append(i)

    for i in range(num):
        for j in range(5):
            if lst[j]==lst3[i]:
                lst2[j]+=1

    print(min(lst2))

func(num,str)