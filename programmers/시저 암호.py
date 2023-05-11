s = "A B z"
n=25
lst = []
for i in s:
    lst.append(ord(i))

ans = ''
for i in lst:
    if i==32:
        ans+=' '
    else:
        if i>=65 and i<=90:
            i+=n
            if i>90:
                i-=26
            ans+=chr(i)
        elif i>=97 and i<=122:
            i+=n
            if i>122:
                i-=26
            ans+=chr(i)

print(ans)