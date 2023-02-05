# https://www.acmicpc.net/problem/18111

# 땅의 높이에 따라 걸리는 최소 시간이 다르다.
# 블록 제거 : 2초 / 블록 삽입 : 1초

# 땅의 높이는 0 ~ 255
# 가로, 세로는 500, 500 = 250,000
# 250,000 * 256 = 64,000,000-> 완전 탐색은 불가능하다.

# 최대한 깎지 않는 방향으로 설계해야 한다.

import sys
from collections import defaultdict

height, width, blocks = map(lambda x: int(x), sys.stdin.readline().split())
numbers = defaultdict(int)
maps = []
for _ in range(height):
    temp = list(map(lambda x: int(x), sys.stdin.readline().split()))
    for num in temp:
        numbers[num] += 1
    maps.append(temp)

result = [sys.maxsize, 0]
for target_height, _ in sorted(numbers.items(), key=lambda x: x[0]):
    inventory = blocks
    time = 0
    for single_map in maps:
        for num in single_map:
            if num > target_height:
                time += (num - target_height) * 2
                inventory += (num - target_height)
            elif num < target_height:
                time += target_height - num
                inventory -= target_height - num
    if inventory < 0:
        continue

    if result[0] > time:
        result = [time, target_height]
print(*result)
