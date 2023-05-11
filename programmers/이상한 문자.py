s = "try hello world"
answer=''
cnt=0
for i in s:
    if i==' ':
        answer+=i
        cnt=0
    else:
        if cnt%2!=0:
            answer+=i.lower()
        else:
            answer+=i.upper()
        cnt+=1
print(answer)