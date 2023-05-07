def func(x,y):
    if x<=11:
        print('280')
    elif x>=12 and x<=16:
        if y==1:
            print('280')
        else:
            print('320')
    else: 
        print('280')

x, y = map(int, input().split())

func(x,y)