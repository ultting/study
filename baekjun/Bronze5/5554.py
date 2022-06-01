# 심부름 가는길
# 학교, pc방, 학원

# 집 - > 학교
# 학교 -> pc방
# pc방 -> 학원
# 학원 -> 집

# 총 이동시간은 60이상 3600초 이하

# x분 y초를 출력

import math

sec = []

for i in range(4):
    sec.append(int(input()))

print(math.floor(sum(sec)/60))
print(sum(sec)%60)