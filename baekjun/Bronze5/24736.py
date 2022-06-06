team = list(map(int, input().split()))
team2 = list(map(int, input().split()))
score = [6,3,2,1,2]
result = 0
result2 = 0
for i in range(len(team)):
    result += team[i] * score[i]    
    result2 += team2[i] * score[i]
print(result)
print(result2)