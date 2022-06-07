# 심부름가는길

import math

sec = []

for i in range(4):
    sec.append(int(input()))

print(math.floor(sum(sec)/60))
print(sum(sec)%60)