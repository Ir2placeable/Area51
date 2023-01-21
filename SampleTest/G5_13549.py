# https://www.acmicpc.net/problem/13549

# 단순 BFS 문제로 보인다. + 비용이 들어가 있으니, -> 다익스트라 알고리즘을 적용한다.

import sys
from collections import deque

n, k = map(lambda x: int(x), sys.stdin.readline().split())

cost = [sys.maxsize for _ in range(100001)]
cost[n] = 0
queue = deque([n])

while queue:
    cur_point = queue.popleft()
    if cur_point == k:
        break

    next_points = []
    if cur_point+1 <= 100000:
        next_points.append(cur_point+1)
    if cur_point-1 >= 0:
        next_points.append(cur_point-1)

    for next_point in next_points:
        if cost[next_point] < cost[cur_point] + 1:
            continue
        cost[next_point] = cost[cur_point] + 1
        queue.append(next_point)

    if cur_point*2 <= 100000:
        next_point = cur_point*2
        if cost[next_point] < cost[cur_point]:
            continue
        cost[next_point] = cost[cur_point]
        queue.append(next_point)

print(cost[k])


