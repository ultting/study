L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

daily = 0

while True:
    daily += 1
    if A > 0 :
        A -= C
    
    if B > 0 :
        B -= D
    
    if A <= 0 and B <= 0 :
        print(L - daily)
        break