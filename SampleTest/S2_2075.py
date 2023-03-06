# https://www.acmicpc.net/problem/2075
import sys, heapq

n = int(sys.stdin.readline())
# queue의 최대 크기는 n으로 고정한다. -> 메모리 떄문이다.
queue = []
for _ in range(n):
    for num in list(map(lambda x: int(x), sys.stdin.readline().split())):
        # queue의 최대 크기에 도달하지 않은 경우
        if len(queue) < n:
            heapq.heappush(queue, num)
            continue

        # queue의 최대 크기에 도달한 경우
        if queue[0] < num:
            heapq.heappush(queue, num)
            heapq.heappop(queue)
print(queue[0])