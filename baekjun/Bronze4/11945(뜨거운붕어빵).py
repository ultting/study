# 뜨거운 붕어빵

# reversed 문제
# reversed 는 int는 안됀다
a, b = map(int, input().split())

for i in range(a):
    fish = input()
    print(''.join(reversed(fish)))