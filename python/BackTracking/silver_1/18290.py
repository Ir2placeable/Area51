# https://www.acmicpc.net/problem/18290
import sys

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def backTracking(y_index, x_index, cur_result, depth):
    global result

    if depth == target_depth:
        result = max(result, cur_result)
        return

    for y in range(y_index, height):
        for x in range(x_index if y == y_index else 0, width):
            if picked[y][x]:
                continue

            if x > 0 and picked[y][x-1]:
                continue
            if x < width-1 and picked[y][x+1]:
                continue
            if y > 0 and picked[y-1][x]:
                continue
            if y > height-1 and picked[y+1][x]:
                continue

            picked[y][x] = True
            backTracking(y, x, cur_result + maps[y][x], depth + 1)
            picked[y][x] = False


height, width, target_depth = map(lambda x: int(x), sys.stdin.readline().split())
maps = [list(map(lambda x: int(x), sys.stdin.readline().split())) for _ in range(height)]
picked = [[False for _ in range(width)] for _ in range(height)]

result = -sys.maxsize
backTracking(0, 0, 0, 0)
print(result)