import sys, heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
maps = [[] for _ in range(n+1)]
total_cost = [sys.maxsize for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(lambda x: int(x), sys.stdin.readline().split())
    maps[a].append([c, b])
start, end = map(lambda x: int(x), sys.stdin.readline().split())

queue = [[0, start]]
total_cost[start] = 0
while queue:
    cur_cost, cur_pos = heapq.heappop(queue)

    if cur_cost > total_cost[cur_pos]:
        continue

    for nex_cost, nex_pos in maps[cur_pos]:
        if cur_cost + nex_cost < total_cost[nex_pos]:
            total_cost[nex_pos] = cur_cost + nex_cost
            heapq.heappush(queue, [cur_cost + nex_cost, nex_pos])
print(total_cost[end])
