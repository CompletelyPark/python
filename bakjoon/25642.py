x, y = map(int, input().split())

while True:
    y+=x
    if y>=5:
        print('yt')
        break
    x+=y
    if x>=5:
        print('yj')
        break

