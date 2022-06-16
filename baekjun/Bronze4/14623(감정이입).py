from unittest import result


# bin 2진수 // oct 8진수 // hex 16진수
# int(input(), x) x = 2 , 8 , 16 에 따라 진수 바뀜
a = int(input(), 2)
b = int(input(), 2)

result = bin(a*b)
print(result[2:])