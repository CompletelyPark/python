import math
import time


from sys import stdin
start = time.time()
t = int(stdin.readline())

def new_func(n):
    lst = []
    for _ in range(n):
        lst.append(list(map(int,stdin.readline().split())))

def new_func1(i):
    print(f'Material Management {i+1}\nClassification ---- End!')

for i in range(t):
    n = int(stdin.readline())
    a, b = map(int,input().split())
   
    new_func(n)

for i in range(t):
    new_func1(i)

end = time.time()
print(end - start)
