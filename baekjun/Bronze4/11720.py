# 숫자의 합

a = int(input())
b = int(input())
bList = list(map(int, str(b)))
c = 0

for i in bList:
    c += i

print(c)