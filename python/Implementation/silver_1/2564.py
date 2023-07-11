# https://www.acmicpc.net/problem/2564

# 1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽

import sys

width, height = map(lambda x: int(x), sys.stdin.readline().split())
n = int(sys.stdin.readline())
stores = []
cur_x, cur_y, cur_d = 0, 0, 0
for i in range(n+1):
    direction, displacement = map(lambda x: int(x), sys.stdin.readline().split())

    x, y = 0, 0
    if direction == 1:
        x, y = displacement, height
    elif direction == 2:
        x, y = displacement, 0
    elif direction == 3:
        x, y = 0, height - displacement
    elif direction == 4:
        x, y = width, height - displacement

    if i == n:
        cur_x, cur_y, cur_d = x, y, direction
        continue
    stores.append([x, y, direction])

square_round = 2 * width + 2 * height
result = 0
case = {2: 4, 4: 2, 1: 3, 3: 1}
for tar_x, tar_y, tar_d in stores:
    diff = 0
    if case[cur_d] == tar_d or cur_d == tar_d:
        diff = abs(tar_x - cur_x) + abs(tar_y - cur_y)
    else:
        diff = tar_x + tar_y + cur_x + cur_y
    result += min(square_round - diff, diff)
print(result)