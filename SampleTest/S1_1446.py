# https://www.acmicpc.net/problem/1446

# 길찾기 + 최소비용 문제 -> 다익스트라 알고리즘
# 다익스트라 -> heapq 사용

# 이 문제의 특징은 지름길을 항상 이용하지 않아도 된다는 것임.
# 한 칸씩 전진하는 경우가 있기 때문에, maps에 한 칸씩 전진하는 경우를 넣고 다익스트라 알고리즘을 시작해야 한다.

import sys
import heapq

n, target = map(lambda x: int(x), sys.stdin.readline().split())
maps = [[] for _ in range(10001)]
for i in range(1000):
    maps[i].append([1, i+1])
for _ in range(n):
    a, b, c = map(lambda x: int(x), sys.stdin.readline().split())
    if b > target:
        continue
    maps[a].append([c, b])

cost = [sys.maxsize for i in range(10001)]
cost[0] = 0
queue = []
heapq.heappush(queue, [0, 0])

while queue:
    cur_cost, cur_location = heapq.heappop(queue)

    for next_cost, next_location in maps[cur_location]:
        if cost[next_location] < cur_cost + next_cost:
            continue

        cost[next_location] = cur_cost + next_cost
        heapq.heappush(queue, [cur_cost + next_cost, next_location])
print(cost[target])