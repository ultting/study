# 타임카드

for i in range(3):
    a = list(map(int, input().split()))
    h1 = a[0] * 3600
    h2 = a[3] * 3600
    m1 = a[1] * 60
    m2 = a[4] * 60
    s1 = a[2]
    s2 = a[5]
    
    resultTime = (h2 - h1) + (m2 - m1) + (s2 - s1)
    h = resultTime//3600
    m = (resultTime%3600)//60
    s = (resultTime%3600)%60
    print(h, m, s)