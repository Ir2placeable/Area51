# https://www.acmicpc.net/problem/2110

import sys

n, c = map(lambda x: int(x), sys.stdin.readline().split())
locations = []
for _ in range(n):
    locations.append(int(sys.stdin.readline()))
locations.sort()

start, end = 1, locations[-1] - locations[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    current = locations[0]
    count = 1

    for i in range(1, n):
        if locations[i] >= current + mid:
            count += 1
            current = locations[i]

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)