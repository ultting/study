# 삼각형 외우기

a = int(input())
b = int(input())
c = int(input())

sum = a + b + c
if a == b == c == 60:
    print("Equilateral")
elif sum != 180:
    print("Error")
elif sum == 180 and a==b or b==c or a==c:
    print("Isosceles")
elif sum == 180 and a!=b or b!=c or a!=c:
    print("Scalene")
