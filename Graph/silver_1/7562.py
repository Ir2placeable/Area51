# 7562 : 나이트의 이동
# https://www.acmicpc.net/problem/7562
import sys
from collections import deque

test_case = int(sys.stdin.readline())

move_cases = [[-2, 1], [-2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2], [2, 1], [2, -1]]
for _ in range(test_case):
    n = int(sys.stdin.readline())
    x1, y1 = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
    x0, y0 = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))

    visited = [[0 for i in range(n)] for j in range(n)]
    visited[x1][y1] = 1

    queue = deque([[x1, y1]])
    while queue:
        x2, y2 = queue.popleft()

        for move_case in move_cases:
            x3, y3 = x2 + move_case[0], y2 + move_case[1]
            if x3 < 0 or x3 > n-1:
                continue
            if y3 < 0 or y3 > n-1:
                continue

            if visited[x3][y3] == 0:
                visited[x3][y3] = visited[x2][y2] + 1
                queue.append([x3, y3])

    print(visited[x0][y0] - 1)
