# 1689 : 겹치는 선분
# https://www.acmicpc.net/problem/1689

import sys, heapq
n = int(sys.stdin.readline())

lines = []
for _ in range(n):
    lines.append(list(map(lambda x: int(x), sys.stdin.readline().split())))
lines.sort()
# print(lines)

# x[0]으로 정렬했기 때문에, x[0]은 항상 앞에 것이 작다.
# 그래서 heap 에는 x[1]만 넣어주면 된다.
heap = [lines[0][1]]
count = 1
for i in range(1, n):
    line = lines[i]
    while heap and heap[0] <= line[0]:
        heapq.heappop(heap)

    heapq.heappush(heap, line[1])
    count = max(count, len(heap))

print(count)