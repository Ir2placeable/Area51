# 13904 : 과제
# https://www.acmicpc.net/problem/13904
import heapq
import sys

n = int(sys.stdin.readline())
items = []
for _ in range(n):
    day, score = map(lambda x: int(x), sys.stdin.readline().split())
    heapq.heappush(items, [-score, day, score])
# items는 score가 큰 순 으로 정렬되어 있다.

scores = [0 for _ in range(1001)]
while items:
    _, day, score = heapq.heappop(items)
    for i in range(day, 0, -1):
        if scores[i] == 0:
            scores[i] = score
            break

print(sum(scores))