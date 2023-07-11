# https://www.acmicpc.net/problem/5212

# 맵을 트리밍 하는 것이 관건이다.
# 맵 트리밍 작업은 max, min 값을 x, y 각각 총 4개를 구한다.

import sys
import copy

height, width = map(lambda x: int(x), sys.stdin.readline().split())
maps = []
for _ in range(height):
    maps.append(list(sys.stdin.readline().rstrip()))
future_maps = copy.deepcopy(maps)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
# 50년 후 결과 만들기
for y in range(height):
    for x in range(width):
        # 현재 위치가 육지일 때
        if maps[y][x] == 'X':
            # 주변 바다의 개수를 센다
            oceans = 0
            for j in range(4):
                # 주변 위치
                ny = y + dy[j]
                nx = x + dx[j]

                # 맵 밖을 벗어나는 경우 / 주변 위치가 바다인 경우
                if ny < 0 or nx < 0 or ny > height - 1 or nx > width - 1 or maps[ny][nx] == '.':
                    oceans += 1
                # 주변 위치 3개 이상이 바다인 경우 -> 미래 지도에는 바다가 된다.
                if oceans == 3:
                    future_maps[y][x] = '.'
                    break

min_x, min_y = 0, 0
max_x, max_y = width-1, height-1

for i in range(0, height):
    if 'X' in future_maps[i]:
        break
    min_y += 1

for i in range(height-1, -1, -1):
    if 'X' in future_maps[i]:
        break
    max_y -= 1

for i in range(0, width):
    if 'X' in [temp[i] for temp in future_maps]:
        break
    min_x += 1

for i in range(width-1, -1, -1):
    if 'X' in [temp[i] for temp in future_maps]:
        break
    max_x -= 1

future_maps = future_maps[min_y : max_y + 1]
for i in range(len(future_maps)):
    print(''.join(future_maps[i][min_x:max_x+1]))