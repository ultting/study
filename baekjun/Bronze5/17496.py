# 스타후르츠

# n 여름의 일수 // t 후르츠 자라는 일수 // c 후르츠 심는 칸 // p 가격
# i+t 일에 수확

n, t, c, p = map(int, input().split())


print((n-1)//t*c*p)
