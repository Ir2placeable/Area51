# https://www.acmicpc.net/problem/3085

# 인접한 두 사탕이 다른 부분을 찾는다.
# 두 사탕을 스왑한다.
# 같은 사탕으로 이루어진 가로 / 세로 의 개수를 센다
    # 최대값을 만들어야 한다.

# 어떤 경우가 최대값인지 모르지 전부 해본다 -> 완전탐색
    # 탐색 : 50 * 50
    # 체크 : 4
    # 최대 1000회 연산 -> 완전탐색 가능

import sys

n = int(sys.stdin.readline())
maps = []
for _ in range(n):
    maps.append(list(sys.stdin.readline().rstrip()))


def checkCandies():
    result = 1
    for y in range(n):
        temp_result = 0
        prev = maps[y][0]
        for x in range(n):
            if maps[y][x] == prev:
                temp_result += 1
            else:
                prev = maps[y][x]
                result = max(result, temp_result)
                temp_result = 1
        result = max(result, temp_result)

    for x in range(n):
        temp_result = 0
        prev = maps[0][x]
        for y in range(n):
            if maps[y][x] == prev:
                temp_result += 1
            else:
                prev = maps[y][x]
                result = max(result, temp_result)
                temp_result = 1
        result = max(result, temp_result)
    return result




max_candy = 1
for y in range(n):
    for x in range(n):
        # 오른쪽으로 바꾸기
        if x+1 < n and maps[y][x] != maps[y][x+1]:
            maps[y][x], maps[y][x+1] = maps[y][x+1], maps[y][x]
            max_candy = max(max_candy, checkCandies())
            maps[y][x], maps[y][x+1] = maps[y][x+1], maps[y][x]

        # 아래로 바꾸기
        if y+1 < n and maps[y][x] != maps[y+1][x]:
            maps[y][x], maps[y+1][x] = maps[y+1][x], maps[y][x]
            max_candy = max(max_candy, checkCandies())
            maps[y][x], maps[y+1][x] = maps[y+1][x], maps[y][x]
print(max_candy)
