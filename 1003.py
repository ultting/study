# 피보나치 함수
# fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
# fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
# 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
# fibonacci(0)은 0을 출력하고, 0을 리턴한다.
# fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
# 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.

t = int(input()) # 1
 
for _ in range(t): # 1
    cnt_0 = [1,0]
    cnt_1 = [0,1]
    n = int(input()) # 5
    if n>1: # 5> 1
        for i in range(n-1): # i = 0 1 2 3
            print("cnt_0",cnt_0)
            print("cnt_1",cnt_1)
            cnt_0.append(cnt_1[-1]) # 0 1
            #print(cnt_1[-1]) # cnt_0 = [1,0,0], [1,0,0,1]
            cnt_1.append(cnt_0[-2]+cnt_1[-1])  # 0 + 1
            #print(cnt_0[-2]) # cnt_1 = [0,1,1], [0,1,1,1]
 
    print(cnt_0[n], cnt_1[n])