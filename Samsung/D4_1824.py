# DFS / BFS + 구현 문제

# 각 위치에서 이동할 수 있는 방향이 4개 이다.

# 40분 컷
# visited 를 각 방향마다 추가로 체크할 수 있도록 3중 리스트로 처리했다. -> 한 바퀴 돌고 다시 돌아오는 경우 탈출 조건에 걸리는 문제가 발생했다.
# mem 을 고려해야 해서 4중 리스트로 처리해야 한다. -> 4중 리스트는 너무 헤비하다는 생각이 들었다. -> set 으로 경우를 체크하는 방법을 사용했다.

from collections import deque

# 우 좌 상 하
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for test_case in range(1, t+1):
    height, width = map(lambda x: int(x), input().split())

    maps = []
    for _ in range(height):
        maps.append(list(input()))

    # visited = [[[0 for _ in range(4)] for _ in range(width)] for _ in range(height)]
    # visited[0][0][0] = 1
    visited = set()
    visited.add((0, 0, 0, 0))

    queue = deque([])
    queue.append([0, 0, 0, 0])
    result = 'NO'

    while queue:
        qy, qx, mem, d = queue.popleft()

        next_directions = []
        command = maps[qy][qx]
        if command == '@':
            result = 'YES'
            break
        elif command == '<':
            next_directions.append(1)
        elif command == '>':
            next_directions.append(0)
        elif command == '^':
            next_directions.append(2)
        elif command == 'v':
            next_directions.append(3)
        elif command == '_':
            if mem == 0:
                next_directions.append(0)
            else:
                next_directions.append(1)
        elif command == '|':
            if mem == 0:
                next_directions.append(3)
            else:
                next_directions.append(2)
        elif command == '?':
            next_directions.append(0)
            next_directions.append(1)
            next_directions.append(2)
            next_directions.append(3)
        elif command == '.':
            next_directions.append(d)
        elif command == '+':
            mem = (mem + 1) % 16
            next_directions.append(d)
        elif command == '-':
            mem = (mem - 1) % 16
            next_directions.append(d)
        else:
            mem = int(command)
            next_directions.append(d)

        for next_direction in next_directions:
            ny = (qy + dy[next_direction]) % height
            nx = (qx + dx[next_direction]) % width

            if (ny, nx, mem, next_direction) in visited:
            # if visited[ny][nx][next_direction] == 1:
                continue

            visited.add((ny, nx, mem, next_direction))
            # visited[ny][nx][next_direction] = 1
            queue.append([ny, nx, mem, next_direction])
    
    print("#%d %s" % (test_case, result))