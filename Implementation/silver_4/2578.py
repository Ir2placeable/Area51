# https://www.acmicpc.net/problem/2578

# 사회자가 부르는 번호를 빙고에서 찾는다 -> 최대 25
# 사회자가 부르는 번호를 받을 때마다 모든 빙고의 경우의 수를 체크한다 -> 1회당 12번 체크한다.
# 번호의 최대 개수 * 빙고에서 번호 찾기 * 모든 빙고의 경우의 수 체크 = 25 * 25 * 12 = 7500
# 완전탐색이 가능하다.

import sys

maps = []
for _ in range(5):
    maps.append(list(map(lambda x: int(x), sys.stdin.readline().split())))

calls = []
for _ in range(5):
    temp = list(map(lambda x: int(x), sys.stdin.readline().split()))
    for i in temp:
        calls.append(i)


def crossNumber(num):
    for x in range(5):
        for y in range(5):
            if maps[x][y] == num:
                maps[x][y] = 0
                return


def countBingo():
    bingo_count = 0
    # 가로 빙고를 체크한다.
    for x in range(5):
        temp = 0
        for y in range(5):
            temp += maps[x][y]
        if temp == 0:
            bingo_count += 1

    # 세로 빙고를 체크한다.
    for y in range(5):
        temp = 0
        for x in range(5):
            temp += maps[x][y]
        if temp == 0:
            bingo_count += 1

    # 하향 대각 빙고를 체크한다.
    temp = 0
    for x in range(5):
        temp += maps[x][x]
    if temp == 0:
        bingo_count += 1

    # 상향 대각 빙고를 체크한다.
    temp = 0
    for x in range(4, -1, -1):
        temp += maps[x][5-x-1]
    if temp == 0:
        bingo_count += 1

    return bingo_count


total_calls = 0
for call in calls:
    total_calls += 1
    # 빙고의 숫자를 지운다.
    crossNumber(call)
    # 빙고의 개수를 구한다.
    cur_bingo = countBingo()
    # 만약 빙고의 개수가 3개 이상이면 중단한다.
    if cur_bingo >= 3:
        break

print(total_calls)