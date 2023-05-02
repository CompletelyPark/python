n = int(input())
lst = list(map(int,input().split()))
prev = 0 # 이전 핸드폰
x = 0 # 소모량
y = 0 # 총 소모된 양

for i in lst:
    if prev!=i:
        x = 2
    else:
        x*=2
    y=y+x
    prev = i

    if y>=100:
        prev = 0
        y = 0
        x = 1
    
print(y)
    
    