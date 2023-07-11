# 1715 : 카드 정렬하기
# https://www.acmicpc.net/problem/1715

# 10, 20, 40 인 경우
# 10 + 20
# 10 + 20 + 40
# 처음 더한 숫자는 계속 더해진다. -> 적은 수는 처음에, 큰 수는 가능하면 나중으로 더한다.
# 우선순위 큐를 사용하면 풀 수 있을 거라 예상. -> heap queue 사용

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
