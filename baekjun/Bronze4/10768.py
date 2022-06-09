# 특별한 날

month = int(input())
daily = int(input())

if month > 2 and daily > 18:
    print("After")
elif month < 2 and daily < 18 :
    print("Before")
elif  month == 2 and daily == 18:
    print("Special")
