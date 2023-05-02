n = int(input())
print('int a;')
print('int *ptr = &a')

for i in range(1,n):
    print('int ',end='')
    for j in range(i+1):
        print('*',end='')
    print('ptr',end='')
    print(i+1,end=' ')
    print('= &ptr',end='')
    if i>=2:
        print(i,end='')
        print(';')
    else:
        print(';')