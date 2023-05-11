n=12345
answer=[]
s = str(n)
for i in s:
    answer.append(i)
answer.reverse()
answer=list(map(int,answer))
print(answer)