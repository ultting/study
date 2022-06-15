A = int(input()) # 현재 온도
B = int(input()) # 목표 온도
C = int(input()) # 얼어있는 고기 1도 데우는데 걸리는 시간
D = int(input()) #얼어있는 고기 해동하는데 걸리는 시간
E = int(input()) #얼지 않은 고기를 1도 데우는데 걸리는 시간

##-10
sec = 0

if A < 0 :
    sec += abs(A) * C
    A -= A
print(A, sec)  
if A == 0 :
    sec += D
print(A, sec)
if A < B :
   sec += (B-A) * E

print(sec)


# 백준 풀이


time = 0
if A < 0:
  time += ((abs(A) * C) + D) + B*E

else:
  time += (B-A) *E

print(time)