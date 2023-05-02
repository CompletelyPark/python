n, m = map(int,input().split())
a, d = map(int,input().split())
sr, sc = map(int,input().split())

i = 1
state = 0
while True:
    if i==n and a==m: break
    '''print(i,a,d)'''

    if d==0: a-=1

    if d==1: a+=1

    if a==0:
        i+=1
        d=1

    if a==m+1:
        i+=1
        d=0

    """print('')
    print(i,a,d)
    print('===================')"""
    if i==sr and a==sc:
        state = 1
    
if state==1: print('NO...')
else: print('YES!')