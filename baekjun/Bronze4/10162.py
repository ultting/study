# 전자레인지
# A = 300초
# B = 60초
# C = 10초
t = int(input())

A = t//300
B = (t%300)//60
C1 = ((t%300)%60)//10
C2 = ((t%300)%60)%10

if C2 == 0 :
    print(A, B, C1)
elif C2 !=0 :
    print(-1)    
