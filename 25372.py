n = int(input())

def new_func(n):
    for _ in range(n):
        str = input()

        if len(str)>=6 and len(str)<=9:
            print('yes')
        else:
            print('no')

new_func(n)