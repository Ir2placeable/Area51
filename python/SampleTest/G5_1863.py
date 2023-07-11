# https://www.acmicpc.net/problem/1863
# 1시간 34분

import sys

n = int(sys.stdin.readline())

result = 0
heights = []
for _ in range(n):
    a, new_height = map(lambda x: int(x), sys.stdin.readline().split())

    # 이전 건물이 없다 -> 새로 건물을 올린다.
    if not heights:
        result += 1
        heights.append(new_height)
        continue

    # 현재 건물이 이전 건물보다 높다 -> 새로 건물을 올린다.
    if heights[-1] < new_height:
        result += 1
        heights.append(new_height)
        continue

    # 현재 건물 높이가 0이다 -> 땅이다 -> 초기화한다.
    if new_height == 0:
        heights = []
        continue

    # 현재 건물이 이전 건물보다 낮다.
    if heights[-1] > new_height:
        # 현재 건물보다 낮은 이전 건물들을 제거한다.
        while heights and heights[-1] > new_height:
            heights.pop()

        # 남은 건물 중에 현재 건물의 높이가 같은 것이 있다 -> 건물이 이어져 있다 -> 아무것도 하지 않는다.
        if heights and heights[-1] == new_height:
            continue

        # 이어진 건물이 없다 -> 새로 건물을 올린다.
        result += 1
        heights.append(new_height)

print(result)
