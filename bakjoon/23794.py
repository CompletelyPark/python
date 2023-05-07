n = int(input())

for _ in range(1, n+3):
    print('@',end='')
print('')

for i in range(1,n+1):
    for j in range(1,n+3):
        if j==1 or j==n+2: print('@',end='')
        else: print(' ',end='')
    print('')
        
for _ in range(1, n+3):
    print('@',end='')
