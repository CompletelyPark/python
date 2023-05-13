p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]
p.sort()
c.sort()
print(p)
print(c)
x = len(p)
a = ''
for i in range(x-1):
    if p[i]!=c[i]:
        a=p[i]
        #return p[i]  
    else:
        a=p[-1]
print(a)
# return p[-1]


'''
collection 함수
zip 함수
else로 했을 때 시간 초과되는 이유
값 할당은 o(1)이지만 else문이 있을 경우 o(x-1)번이 진행돼서
총 시간 복잡도가 o(n)이 돼서 초과되는 거 같다
'''