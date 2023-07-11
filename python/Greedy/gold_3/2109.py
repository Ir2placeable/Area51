# 2109 : 순회강연
# https://www.acmicpc.net/problem/2109
import sys
import heapq

n = int(sys.stdin.readline())
schedules = []
for _ in range(n):
    p, d = map(lambda x: int(x), sys.stdin.readline().split())
    heapq.heappush(schedules, [-p, p, d])
# print(schedules)

costs = [0 for _ in range(10001)]
while schedules:
    _, p, d = heapq.heappop(schedules)
    for i in range(d, 0, -1):
        if costs[i] == 0:
            costs[i] = p
            break
print(sum(costs))