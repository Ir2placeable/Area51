# https://www.acmicpc.net/problem/1927

import heapq, sys

n = int(sys.stdin.readline())
queue = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not queue:
            print(0)
            continue
        print(heapq.heappop(queue))
        continue

    heapq.heappush(queue, x)