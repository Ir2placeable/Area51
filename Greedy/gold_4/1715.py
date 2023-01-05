# 1715 : 카드 정렬하기
# https://www.acmicpc.net/problem/1715

# 10, 20, 40 인 경우
# 10 + 20
# 10 + 20 + 40
import sys
import heapq

n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    heapq.heappush(numbers, int(sys.stdin.readline()))

result = 0
while len(numbers) > 1:
    a = heapq.heappop(numbers)
    b = heapq.heappop(numbers)
    c = a + b
    result += c
    heapq.heappush(numbers, c)

print(result)
