
sum = 0

for i in range(5):
    team = int(input())
    
    if team < 40:
        team = 40
    
    sum += team

print(sum//5)
