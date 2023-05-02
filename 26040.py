str = input()
lst=list(input().split())

def func(str,list): 
    str1=''
    for x in str:
        if x in lst:
            str1+=x.lower()
        else:
            str1+=x

    return str1
    
print(func(str,lst))
