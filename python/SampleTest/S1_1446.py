# https://www.acmicpc.net/problem/1446
import sys, heapq

n, d = map(lambda x: int(x), sys.stdin.readline().split())
shortcuts = [list(map(lambda x: int(x), sys.stdin.readline().split())) for _ in range(n)]

edges_in_node = [[[1, i+1]] for i in range(d+1)]
for start, end, cost in shortcuts:
    # 고속도로 범위를 벗어나는 경우
    if end > d:
        continue
    edges_in_node[start].append([cost, end])

queue = [[0, 0]]
result = 0

while queue:
    current_cost, current_position = heapq.heappop(queue)
    if current_position == d:
        result = current_cost
        break

    for add_cost, next_position in edges_in_node[current_position]:
        heapq.heappush(queue, [current_cost + add_cost, next_position])

print(result)