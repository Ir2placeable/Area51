# 12782 : 비트 우정지수
# https://www.acmicpc.net/problem/12782

test_case = int(input())

for i in range(0, test_case):
    origin, target = input().split(" ")

    a, b, diff = 0, 0, 0
    for j in range(0, len(origin)):
        if origin[j] == '1':
            a += 1
        if target[j] == '1':
            b += 1

        if origin[j] != target[j]:
            diff += 1

    print((max(a-b, b-a) + diff)//2)
