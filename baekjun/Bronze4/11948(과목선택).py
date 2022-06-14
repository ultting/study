# 과목선택

example = []

for i in range(6):
    score = int(input())
    example.append(score)
    
four = example[0:4]
two = example[4:6]
four.sort(reverse=True)
two.sort(reverse=True)
print(sum(four[0:3],two[0]))