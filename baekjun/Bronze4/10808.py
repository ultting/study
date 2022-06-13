# 알파벳 개수

S = input()
english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
hello = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for j in range(len(english)):
    for i in S:
        if i == english[j]:
            hello[j] += 1
                        
for i in range(len(hello)):
    print(hello[i], end=' ')



# 백준 다른사람 풀이
## 아스키 코드 활용
s = input()
lst = [0]*26
for i in s:
    lst[ord(i)-97]+=1
for i in lst:
    print(i,end= ' ')
    
    
# 출처: https://imksh.com/38 [강승현입니다:티스토리]    