x, y = map(int, input().split())
lst=list(map(int,input().split()))
state=0

while True:
    for i in range(x):
        if lst[i]<y:
            print(i+1)
            state=1
            break
        else:
            y+=1

    if state==1:
        break

        
