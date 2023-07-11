
import heapq
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

weights = [[] for _ in range(n+1)]
total_weights = [sys.maxsize for _ in range(n+1)]
for _ in range(m):
    start, end, weight = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
    weights[start].append([weight, end])

start, end = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))

queue = [[0, start]]
total_weights[start] = 0
while queue:
    cur_weight, cur_point = heapq.heappop(queue)

    # total_weight 보다 현재 weight 가 큰 경우 -> 수정할 내용 자체가 없으니 넘어간다.
    if total_weights[cur_point] < cur_weight:
        continue

    # 현재 위치에서 넘어갈 수 있는 다음 위치를 모두 탐색한다.
    for w, next_point in weights[cur_point]:
        next_weight = cur_weight + w
        # 다음 위치로 가는 비용이 더 적다면, 해당 위치에서 새로 탐색한다.
        if next_weight < total_weights[next_point]:
            total_weights[next_point] = next_weight
            heapq.heappush(queue, [next_weight, next_point])

print(total_weights[end])

