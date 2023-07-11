# 1783 : 병든 나이트
# https://www.acmicpc.net/problem/1783
import sys
from collections import deque
height, width = map(lambda x: int(x), sys.stdin.readline().split(" "))

history = set()
history.add((0, 0))
queue = deque([(0, 0)])

dx = [1, 2, 2, 1]
dy = [2, 1, -1, -2]

while queue:
    qx, qy = queue.popleft()

    for i in range(4):
        nx = qx + dx[i]
        ny = qy + dy[i]

        if nx < 0 or ny < 0 or nx > width-1 or ny > height-1:
            continue

        if (nx, ny) in history:
            continue

        print((nx, ny))
        history.add((nx, ny))
        queue.append((nx, ny))

print(len(history))