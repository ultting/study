
b = ['a', 'e', 'i', 'o', 'u']

while True:
    cnt = 0
    s = list(input().lower())
    if s[0] == '#':
        break
    for i in s :
        if i in b:
            cnt += 1
    print(cnt)

            
