# https://www.acmicpc.net/problem/1189
import sys

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(cur_y, cur_x, length):
    global result

    if length == target:
        if cur_y == 0 and cur_x == width - 1:
            result += 1
        return

    for i in range(4):
        ny = cur_y + dy[i]
        nx = cur_x + dx[i]

        if ny < 0 or nx < 0 or ny > height - 1 or nx > width - 1 or maps[ny][nx] == 'T':
            continue
        if visited[ny][nx]:
            continue

        visited[ny][nx] = True
        dfs(ny, nx, length + 1)
        visited[ny][nx] = False


height, width, target = map(lambda x: int(x), sys.stdin.readline().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(height)]
visited = [[False for _ in range(width)] for _ in range(height)]
visited[height-1][0] = True

result = 0
dfs(height-1, 0, 1)
print(result)