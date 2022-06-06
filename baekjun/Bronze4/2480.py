# 1. 3개 == 10000 + 주사위눈 * 1000
# 2. 2개 == 1000 + 주사위눈 * 100
# 3. 모두 다른 눈 == 가장 큰 눈 + 100

a, b, c= map(int, input().split())

if a == b == c :
    print(10000 + a * 1000)
elif a == b or a == c :
    print(1000 + a * 100)
elif b == c :
    print(1000 + b * 100)
else : 
    print(100 * max(a,b,c))
    

