# https://www.acmicpc.net/problem/27983

import math

n = int(input()) # Number of Ribbons input 

lst1 = list(map(int,input().split())) # Ribbons point
lst2 = list(map(int,input().split())) # Ribbons length 
lst3 = list(input().split())          # Ribbons color

ans='NO'    # answer
c1 = 0      # answer Ribbons index 1
c2 = 0      # answer Ribbons index 2

for i in range(n-1):
    for j in range(1,n):
        x = abs(lst1[i] - lst1[j])   # |xi - xj|
        y = lst2[i] + lst2[j]        # Li + Lj (i != j)
        if x<=y and lst3[i]!=lst3[j]: 
            ans='YES'
            c1 = i+1
            c2 = j+1

print(ans)
if ans == 'YES':
    print(c1, c2)

# 