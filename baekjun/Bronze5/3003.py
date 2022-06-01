# 킹, 퀸, 룩, 비숍, 나이트, 폰
result = [1, 1, 2, 2, 2, 8] # 16개 피스
hyuk = list(map(int, input().split())) # 동혁이가 가지고있는 체스말

for i in range(len(result)):
    print(result[i]-hyuk[i])

