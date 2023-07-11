# 구현

# 30분 초과 실패!
# 인접한 변에 지뢰가 없는 것 체크!
# 나머지 체크!

from collections import deque

def getAdjacent(x, y):
    dy = [1, 1, 1, 0, 0, -1, -1, -1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    adjacent_list = []
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > map_size-1 or ny > map_size-1:
            continue

        adjacent_list.append([nx, ny])
    return adjacent_list


def getMinesAdjacent(x, y):
    mines = 0
    for a, b in getAdjacent(x, y):
        if maps[a][b] == '*':
            mines += 1
    return mines


t = int(input())
for test_case in range(1, t+1):
    map_size = int(input())
    maps = []
    for _ in range(map_size):
        maps.append(list(input()))

    result = 0
    # 모든 위치를 순회하며 주변에 지뢰가 없는 땅을 처리한다.
    for x in range(map_size):
        for y in range(map_size):
            if maps[x][y] != '.' or getMinesAdjacent(x, y) != 0:
                continue

            # 주변에 지뢰가 없는 땅인 경우
            result += 1
            maps[x][y] = 0

            # 연쇄작용을 발생시킨다.
            queue = deque(getAdjacent(x, y))
            while queue:
                nx, ny = queue.popleft()
                if maps[nx][ny] != '.':
                    continue

                if maps[nx][ny] != '.' or getMinesAdjacent(nx, ny) == 0:
                    queue += deque(getAdjacent(nx, ny))

                maps[nx][ny] = getMinesAdjacent(nx, ny)

    # 모든 위치를 순회하며 남아있는 위치를 처리한다.
    for x in range(map_size):
        for y in range(map_size):
            if maps[x][y] == '.':
                result += 1

    print("#%d %d" % (test_case, result))