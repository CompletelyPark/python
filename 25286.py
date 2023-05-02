n = int(input())
lst=[]

def new_func(n, lst):
    for _ in range(n):
        x,y = map(int,input().split())
        ansx = 0
        ansy = 0
        ansd = 0
        if (x%400==0) or (x%100!=0 and (x%4==0)):
            if y==3:
                ansx = x
                ansy = y-1
                ansd = 29
            elif y==5 or y==7 or y==10 or y==12:
                ansx = x
                ansy = y-1
                ansd = 30

            elif y==1:
                ansx = x-1
                ansy = 12
                ansd = 31
            else:
                ansx = x
                ansy = y-1
                ansd = 31
        else:
            if y==3:
                ansx = x
                ansy = y-1
                ansd = 28
            elif y==5 or y==7 or y==10 or y==12:
                ansx = x
                ansy = y-1
                ansd = 30
            elif y==1:
                ansx = x-1
                ansy = 12
                ansd = 31
            else:
                ansx = x
                ansy = y-1
                ansd = 31
        lst.append([ansx,ansy,ansd])

new_func(n, lst)

for i in range(n):
    for j in range(3):
        print(lst[i][j],end=' ')
    print('')