# https://www.acmicpc.net/problem/13549

import heapq, sys

x, target = map(lambda x: int(x), sys.stdin.readline().split())
total_cost = [sys.maxsize for i in range(100001)]
total_cost[x] = 0

queue = [[0, x]]
result = 0

while queue:
    current_cost, current_location = heapq.heappop(queue)
    if current_location != 0 and target % current_location == 0:
        result = current_cost
        break

    # 일반 이동 체크
    next_cases = []
    # 다음 위치가 x-1 인 경우
    if current_location > 0:
        next_cases.append([current_cost + 1, current_location - 1])
    # 다음 위치가 x+1 인 경우
    if current_location < 100000:
        next_cases.append([current_cost + 1, current_location + 1])

    for next_cost, next_location in next_cases:
        # 이미 과거의 왔던 비용보다, 현재 든 비용이 큰 경우
        if total_cost[next_location] < next_cost:
            continue
        total_cost[next_location] = next_cost
        heapq.heappush(queue, [next_cost, next_location])

    # 순간 이동 체크
    if 0 < current_location <= 50000:
        for next_location in range(current_location, 100001, current_location):
            if total_cost[next_location] < current_cost:
                continue
            total_cost[next_location] = current_cost
        heapq.heappush(queue, [current_cost, current_location * 2])

print(result)