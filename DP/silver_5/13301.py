# 13301 : 타일 장식물
# https://www.acmicpc.net/problem/13301

k = int(input())

a = 4
b = 6

if k == 1:
    print(a)
elif k == 2:
    print(b)
elif k > 2:
    while k > 2:
        a, b = b, a+b
        k -=1

    print(b)