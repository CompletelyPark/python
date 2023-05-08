n = int(input())
lst = [1,2,3,4,5,6,7,8,9,10,11,12]

def new_func(n, lst):
    st1=0 # 시간
    st2=0 # 월일
    for _ in range(n):
        x,y=map(int,input().split())

        if x>=0 and x<=23:
            if y>=0 and y<=59: st1 = 1
            else: st1 = 0
        elif x>=24: st1 = 0


        if x in lst:
            if x==2:
            #print('2')
                if y>=1 and y<=29: st2=1
                else: st2=0
            elif x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
            #print('135781012')
                if y>=1 and y<=31: st2 =1
                else: st2=0
            else:
            #print('나머지')
                if y>=1 and y<=30: st2 =1
                else: st2=0
        else: st2 = 0

        if st1 == 0 and st2==0: print('No No')
        elif st1==0 and st2==1: print('No Yes')
        elif st1==1 and st2==0: print('Yes No')
        else: print('Yes Yes')

new_func(n, lst)