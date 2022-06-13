# 일급 비밀 !


# reverse() == list로 변환하여 사용
# reversed() == 사용 시 object로 생성

# 두 함수 다 ''.join(reversed()) 를 사용


while True:
    a = input()
    
    if a == "END":
        print("END")
        break
    else :
        print(''.join(reversed(a)))
        
    
    
    
    
