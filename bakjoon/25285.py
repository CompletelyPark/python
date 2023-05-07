n = int(input())
lst = []

for _ in range(n):
    state=0
    x,y=map(float,input().split())

    if x<140.1: state = 6
    elif x<146: state = 5
    elif x<159: state = 4

    elif (x>=159 and x<161):
        x= x/100
        x *=x
        bmi = y/x
        if (bmi >= 16.0) and (bmi < 35.0): state = 3
        else: state = 4   

    elif (x>=161) and (x<204):
        x= x/100
        x *=x
        bmi = y/x
        if (bmi >= 20.0) and (bmi < 25.0): state = 1
        elif ((bmi >= 30.0) and (bmi < 35.0)) or ((bmi >= 16.0) and (bmi < 18.5)): 
            state = 3 
        elif ((bmi >= 18.5) and (bmi < 20.0)) or ((bmi >= 25.0) and (bmi < 30.0)): 
            state = 2
        else: state = 4
    
    elif x>=204: state = 4

    lst.append(state)

for i in lst:
    print(i)