n=2
m=5
max = 1
for i in range(1,n+1):
    if n%i==0 and m%i==0:
        max = i
while m>0:
    t = n
    n = m
    m = t%m

print(n)
# a = n//max
# b = m//max

# x = a*b*max
# answer=[max,x]
# print(answer)