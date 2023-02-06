# https://www.acmicpc.net/problem/18111

# 땅의 높이에 따라 걸리는 최소 시간이 다르다.
# 블록 제거 : 2초 / 블록 삽입 : 1초

# 땅의 높이는 0 ~ 255
# 가로, 세로는 500, 500 = 250,000
# 250,000 * 256 = 64,000,000

import sys
height, width, inventory = map(lambda x: int(x), sys.stdin.readline().split())
maps = []

for _ in range(height):
    maps.append(list(map(lambda x: int(x), sys.stdin.readline().split())))

result = [sys.maxsize, 0]
for target_height in range(257):
    time = 0
    temp_inventory = inventory
    for y in range(height):
        for x in range(width):
            location = maps[y][x]
            if location > target_height:
                time += 2 * (location - target_height)
                temp_inventory += location - target_height
            elif location < target_height:
                time += target_height - location
                temp_inventory -= (target_height - location)

    if temp_inventory < 0:
        continue

    if result[0] >= time:
        result = [time, target_height]

print(*result)