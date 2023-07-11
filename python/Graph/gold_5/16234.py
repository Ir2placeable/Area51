# 16234 : 인구 이동
# https://www.acmicpc.net/problem/16234
import sys
from collections import deque

# 1. BFS 이용, 연합국 끼리 구분한다. -> 이때, 연합국 위치를 따로 저장한다.
# 2. 연합국의 인구수를 조정한다.
# 3. 무한 루프로 1,2 번을 반복한다.
# 4. 만약 구분할 연합국이 없는 경우 종료한다.

n, l, r = map(lambda x: int(x), sys.stdin.readline().split())

population = []
for i in range(n):
    population.append(list(map(lambda x: int(x), sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    return_list = []
    queue = deque([[x, y]])
    return_list.append([x, y])
    while queue:
        qx, qy = queue.popleft()

        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and gate[nx][ny] == 0:
                diff = abs(population[qx][qy] - population[nx][ny])
                if l <= diff <= r:
                    gate[nx][ny] = 1
                    queue.append([nx, ny])
                    return_list.append([nx, ny])

    return return_list


days = 0
while True:
    # 연합국이 있다는 플래그
    departed = False
    # 연합국을 구분한 결과
    gate = [[0 for i in range(n)] for j in range(n)]

    # 모든 위치를 탐색한다.
    for x in range(n):
        for y in range(n):
            if gate[x][y] == 0:
                gate[x][y] = 1

                # BFS 로 연합을 생성한다.
                union_location = bfs(x, y)

                # 연합국의 인구수를 조정한다.
                if len(union_location) > 1:
                    departed = True
                    avg_population = sum(population[a][b] for a, b in union_location) // len(union_location)
                    for a, b in union_location:
                        population[a][b] = avg_population

    # 연합국이 없는 상태
    if not departed:
        break
    days += 1

print(days)
