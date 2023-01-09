# 13975 : 파일 합치기 3
# https://www.acmicpc.net/problem/13975

# 소팅 후, 최소 비용인 것 먼저 계산하기
# 이떄, 우선순위 큐를 사용해야 함 -> 중복된 비용이 있을 수 있음.
import heapq
import sys

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n = int(sys.stdin.readline())
    costs = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
    heapq.heapify(costs)

    total_cost = 0
    while len(costs) > 1:
        cost1 = heapq.heappop(costs)
        cost2 = heapq.heappop(costs)

        cost3 = cost1 + cost2
        total_cost += cost3
        heapq.heappush(costs, cost3)

    print(total_cost)