# 상근날드

s = int(input())
j = int(input())
h = int(input())
cola = int(input())
cidar = int(input())

# 모든가격 100 이상 2000 이하

s1 = s + cola - 50
s2 = s + cidar - 50
j1 = j + cola - 50
j2 = j + cidar - 50
h1 = h + cola - 50
h2 = h + cidar - 50

if s1 <= 2000 or s2 <= 2000 or j1 <= 2000 or j2 <= 2000 or h1 <= 2000 or h2<= 2000 :
    print(min(s1,s2,j1,j2,h1,h2))
    
    

# 백준 사이트 풀이
a = []
b = []
for i in range(3):
    a.append(int(input()))
for i in range(2):
    b.append(int(input()))

a.sort()
b.sort()

print(a[0]+b[0]-50)