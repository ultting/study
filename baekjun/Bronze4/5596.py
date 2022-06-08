min = list(map(int, input().split()))
man = list(map(int, input().split()))

kuk = sum(min)
sea = sum(man)

if kuk > sea :
    print(kuk)
elif kuk < sea :
    print(sea)
elif kuk == sea :
    print(kuk)
    
## 백준 풀이

s = list(map(int,input().rstrip().split()))
t = list(map(int,input().rstrip().split()))

if sum(t) > sum(s):
  print(sum(t))
else:
  print(sum(s))