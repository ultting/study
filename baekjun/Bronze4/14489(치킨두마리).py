a, b = map(int,input().split())
c = 2 * int(input())

if a+b < c:
    print(a+b)
elif a+b >= c:
    print(a+b-c)