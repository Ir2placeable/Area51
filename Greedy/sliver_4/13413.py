# 13413 : 오셀로 재배치
# https://www.acmicpc.net/problem/13413

test_case = int(input())

for test_index in range(0, test_case):
    rocks = int(input())
    origin = input()
    target = input()

    diff = 0
    b_origin, b_target = 0, 0
    for i in range(0, rocks):
        if origin[i] == 'B':
            b_origin += 1
        if target[i] == 'B':
            b_target += 1

        if origin[i] != target[i]:
            diff += 1

    moves = max(b_origin-b_target, b_target-b_origin) + diff
    print(moves // 2)
