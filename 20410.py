# https://www.acmicpc.net/problem/20410

m, seed, x1, x2 = map(int,input().split())

alst=[]
clst=[]

for i in range(m):
    for j in range(m):
        if ((i*seed + j) % m) == x1:
            # print('a = %d'%i)
            # print('c = %d'%j)
            alst.append(i)
            clst.append(j)
#     print('')
# print(len(alst))
# print(len(clst))
a = 0
c = 0
cnt = len(alst)

for i in range(cnt):
    if (alst[i]*x1 + clst[i]) % m == x2:
        a = alst[i]
        c = clst[i]
        break;
print(a,c)