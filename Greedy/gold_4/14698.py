# 14698 : 전생했더니 슬라임 연구자였던 건에 대하여 (Hard)
# https://www.acmicpc.net/problem/14698

# 아주 쉬운 최소값 문제이다. A * B의 총 합이 작아야한다.
# 따라서, A, B가 최소값 이어야한다.
# 당연히 우선순위 큐를 사용한다.

import sys
import heapq

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n = int(sys.stdin.readline())
    slimes = list(map(lambda x: int(x), sys.stdin.readline().split()))
    slimes.sort()

    energy = 1
    while len(slimes) > 1:
        a = heapq.heappop(slimes)
        b = heapq.heappop(slimes)
        c = a * b

        energy *= c
        heapq.heappush(slimes, c)
    energy = energy % 1000000007
    if energy == 1:
        energy = 1
    print(energy)