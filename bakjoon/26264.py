def func():
    cnt1 = 0 
    cnt2 = 0
    str = input()
    cnt1 = str.count('security')
    cnt2 = str.count('bigdata')
    if cnt1>cnt2:
        print('security! ')
    elif cnt1<cnt2:
        print('bigdata? ')
    else:
        print('bigdata? security!')

num = input()
num = int(num)
func()