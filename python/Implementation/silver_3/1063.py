# https://www.acmicpc.net/problem/1063

import sys

king_location, stone_location, n = sys.stdin.readline().split()
moves = []
for _ in range(int(n)):
    moves.append(sys.stdin.readline().rstrip())

dx = {'R': 1, 'L': -1, 'B': 0, 'T': 0, 'RT': 1, 'LT': -1, 'RB': 1, 'LB': -1}
dy = {'R': 0, 'L': 0, 'B': -1, 'T': 1, 'RT': 1, 'LT': 1, 'RB': -1, 'LB': -1}

# 65 <= x <= 72, ALL integer
king_x_cur = ord(king_location[0])
king_y_cur = int(king_location[1])
stone_x_cur = ord(stone_location[0])
stone_y_cur = int(stone_location[1])

for move in moves:
    king_x_next = king_x_cur + dx[move]
    king_y_next = king_y_cur + dy[move]

    # 킹의 위치가 맵을 벗어나는 경우
    if king_x_next < 65 or king_y_next < 1 or king_x_next > 72 or king_y_next > 8:
        continue

    # 킹의 위치가 스톤에 있는 경우
    if king_x_next == stone_x_cur and king_y_next == stone_y_cur:
        stone_x_next = stone_x_cur + dx[move]
        stone_y_next = stone_y_cur + dy[move]

        # 스톤의 위치가 맵을 벗어나는 경우
        if stone_x_next < 65 or stone_y_next < 1 or stone_x_next > 72 or stone_y_next > 8:
            continue

        stone_x_cur = stone_x_next
        stone_y_cur = stone_y_next

    king_x_cur = king_x_next
    king_y_cur = king_y_next

print(chr(king_x_cur) + str(king_y_cur))
print(chr(stone_x_cur) + str(stone_y_cur))