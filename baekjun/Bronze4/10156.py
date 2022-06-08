# 과자

k, n, m = map(int, input().split())

money = k * n
result = money - m

if result >= 0 :
    print(result)
elif result < 0 :
    print(0)