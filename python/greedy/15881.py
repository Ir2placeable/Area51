# 15881 : Pen Pineapple Apple Pen
# https://www.acmicpc.net/problem/15881

# 사과 : A
# 파인애플 : P
# 펜 : p

# 첫 줄 : 목록의 길이 n
# 패턴 : pPAp

n = int(input())
string = input()

target = 'pPAp'
count = 0
i = 0
while i < n-3:
    guess = string[i:i+4]
    if guess == target:
        count += 1
        i += 4
    else :
        i += 1

print(count)