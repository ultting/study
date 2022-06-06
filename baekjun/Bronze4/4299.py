a, b = map(int, input().split())

if a-b < 0 or (a-b)%2 != 0: # 3-1 = 2 < 0 or 2%2 != 0
    print(-1)
else:
    c = (a+b) // 2
    d = (a-b) // 2
    print(max(c, d), min(c, d))