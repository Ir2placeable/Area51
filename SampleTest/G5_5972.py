# https://www.acmicpc.net/problem/5972

# 최소비용 길찾기 문제 -> 다익스트라 알고리즘
# 다익스트라 알고리즘 -> BFS + heapqQ

import sys
import heapq

n, m = map(lambda x: int(x), sys.stdin.readline().split())
maps = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(lambda x: int(x), sys.stdin.readline().split())
    maps[a].append([c, b])
    maps[b].append([c, a])
# maps[start] = [[cost, end], [cost, end]] 형식이다.

# queue = [cost, start]
queue = [[0, 1]]
total_cost = [sys.maxsize for _ in range(n+1)]
total_cost[1] = 0

while queue:
    cur_cost, start = heapq.heappop(queue)

    for add_cost, end in maps[start]:
        if total_cost[end] <= cur_cost + add_cost:
            continue

        total_cost[end] = cur_cost + add_cost
        heapq.heappush(queue, [cur_cost + add_cost, end])
print(total_cost[n])
