# 10부제

car = int(input())
daily = list(map(int, input().split()))

law = 0
for i in daily :
    if car == i :
        law += 1

print(law)