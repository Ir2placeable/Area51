# 25418 : 정수 a를 k로 만들기
# https://www.acmicpc.net/problem/25418

a, k = map(lambda x: int(x), input().split(" "))

move = 0
while a != k:
    if k % 2 == 1:
        k -= 1
    elif k // 2 >= a:
        k //= 2
    else:
        k -= 1
    move += 1

print(move)

