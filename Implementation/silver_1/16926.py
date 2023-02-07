# https://www.acmicpc.net/problem/16926
import sys

height, width, k = map(lambda x: int(x), sys.stdin.readline().split())
maps = []
for _ in range(height):
    maps.append(list(map(lambda x: int(x), sys.stdin.readline().split())))

for _ in range(k):
    for edge_index in range(min(height, width) // 2):
        base_x, base_y = edge_index, edge_index
        displacement_x, displacement_y = width - 2 * edge_index, height - 2 * edge_index
        temp = maps[base_y][base_x]

        for y in range(base_y + 1, base_y + displacement_y):
            origin = maps[y][base_x]
            maps[y][base_x] = temp
            temp = origin

        for x in range(base_x + 1, base_x + displacement_x):
            origin = maps[base_y + displacement_y - 1][x]
            maps[base_y + displacement_y - 1][x] = temp
            temp = origin

        for y in range(base_y + displacement_y - 2, base_y - 1, -1):
            origin = maps[y][base_x + displacement_x - 1]
            maps[y][base_x + displacement_x - 1] = temp
            temp = origin

        for x in range(base_x + displacement_x - 2, base_x - 1, -1):
            origin = maps[base_y][x]
            maps[base_y][x] = temp
            temp = origin

for single_map in maps:
    print(*single_map)