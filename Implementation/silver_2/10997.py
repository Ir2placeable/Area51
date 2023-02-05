# https://www.acmicpc.net/problem/10997

# 한 변의 길이 2n - 1
# 0 : 왼쪽 / 1 : 아래 / 2 : 오른쪽 / 3 : 위
import sys

n = int(sys.stdin.readline())
if n == 1:
    print('*')
else:
    maps = [[' ' for _ in range(4 * n - 3)] for _ in range(4 * n - 1)]

    x, y, d = 4 * n - 4, 0, 0
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]

    min_x, min_y = 0, 0
    max_x, max_y = 4*n-4, 4*n-2

    while True:
        maps[y][x] = '*'

        # 방향 전환
        if d == 0 and x == min_x:
            d = (d + 1) % 4
            min_y += 2
        elif d == 1 and y == max_y:
            d = (d + 1) % 4
            min_x += 2
        elif d == 2 and x == max_x:
            d = (d + 1) % 4
            max_y -= 2
        elif d == 3 and y == min_y:
            d = (d + 1) % 4
            max_x -= 2

        if min_x > max_x:
            break

        x = x + dx[d]
        y = y + dy[d]

    for temp in maps:
        target = 0
        for i in range(len(temp)-1, -1, -1):
            if temp[i] == '*':
                target = i
                break
        print(''.join(temp[:i+1]))