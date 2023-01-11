# 16234 : 인구 이동
# https://www.acmicpc.net/problem/16234
import sys
from collections import deque

# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.

# 1. BFS 이용, 연합국 끼리 구분한다.
# 2. 연합국의 인구수를 조정한다.
# 3. 1,2 번을 반복한다.
# 4. 만약 구분할 연합국이 없는 경우 종료한다.

n, l, r = map(lambda x: int(x), sys.stdin.readline().split())

population = []
for i in range(n):
    population.append(list(map(lambda x: int(x), sys.stdin.readline().split())))
# print(population)

days = 0
while True:
    # 연합국을 구분한 결과
    gate = [[0 for i in range(n)] for j in range(n)]
    gate_index = 1

    # 모든 위치를 탐색한다.
    for x in range(n):
        for y in range(n):
            if gate[x][y] == 0:
                gate[x][y] = gate_index

                # BFS 로 연합을 생성한다.
                union_population = population[x][y]
                union_location = deque([[x, y]])
                queue = deque([[x, y]])
                while queue:
                    qx, qy = queue.popleft()

                    for _x in range(max(0, qx-1), min(n, qx+2)):
                        # 이미 처리되었거나 다른 연합인 경우 지나간다.
                        if gate[_x][qy] != 0:
                            continue
                        # 인구 차이
                        diff = max(population[qx][qy] - population[_x][qy], population[_x][qy] - population[qx][qy])
                        if l <= diff <= r:
                            gate[_x][qy] = gate_index
                            queue.append([_x, qy])
                            union_population += population[_x][qy]
                            union_location.append([_x, qy])

                    for _y in range(max(0, qy-1), min(n, qy+2)):
                        if gate[qx][_y] != 0:
                            continue
                        diff = max(population[qx][qy] - population[qx][_y], population[qx][_y] - population[qx][qy])
                        if l <= diff <= r:
                            gate[qx][_y] = gate_index
                            queue.append([qx, _y])
                            union_population += population[qx][_y]
                            union_location.append([qx, _y])

                # 연합국의 인구수를 조정한다.
                avg_population = union_population // len(union_location)
                while union_location:
                    ux, uy = union_location.popleft()
                    population[ux][uy] = avg_population

                gate_index += 1

    # 연합국이 없는 상태
    if gate[-1][-1] == n*n:
        break

    days += 1

print(days)
