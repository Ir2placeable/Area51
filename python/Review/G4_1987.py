# 말이 최대한 이동할 수 있는 거리를 재는 문제이다.
# 지나온 알파벳을 하나씩 저장하면서 풀면 될 것 같지만 그렇지 않다.
# 말의 현재 위치에 따라 지금까지 지나온 알파벳을 저장해야 한다.
# BFS / DFS 문제이다.

# 말의 현재 위치에 따라 지금까지 지나온 알파벳을 저장하는 방법
    # path를 set으로 사용하면, 초기 메모리의 사용이 많아진다. 그러나 탐색이 빠르다.
    # path를 list로 사용하면, 메모리가 필요한 만큼 사용된다. 그러나 완전탐색이 필요하다.
    # path를 defaultdict로 사용하면, 초기 메모리를 줄이고 단일탐색이 가능하다. 그러나 메모리 초과가 발생했다.
# 현재 위치에 따라 path를 모두 저장하는 방법은 메모리 초과가 발생한다. -> path를 하나만 두고 사용해야 한다.

# 이 문제에서는 visited가 필요하지 않다. visited의 역할을 path가 수행하기 때문이다.

import sys
from collections import defaultdict

height, width = map(lambda x: int(x), sys.stdin.readline().split())
maps = []
for _ in range(height):
    maps.append(list(sys.stdin.readline().rstrip()))

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

defaultPath = maps[0][0]
queue = set()
queue.add((0, 0, defaultPath))
result = 1

while queue:
    qy, qx, path = queue.pop()

    for i in range(4):
        ny = qy + dy[i]
        nx = qx + dx[i]

        if ny < 0 or nx < 0 or ny > height-1 or nx > width-1:
            continue

        if maps[ny][nx] in path:
            continue

        next_path = path[:] + maps[ny][nx]
        queue.add((ny, nx, next_path))
        result = max(result, len(next_path))
print(result)