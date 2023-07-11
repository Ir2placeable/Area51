# 13549 : 숨바꼭질 3
# https://www.acmicpc.net/problem/13549

# 걸으면 +1 / -1 비용 1
# 순간이동하면 *2 비용 0
import sys
from collections import deque

n, k = map(lambda x: int(x), sys.stdin.readline().split())
visited = [100001 for _ in range(100001)]
visited[n] = 0

queue = deque([n])
time = 0
while queue:
    location = queue.popleft()
    if location == k:
        time = visited[location]
        break

    next_locations = []

    if location*2 <= 100000:
        next_locations.append(location * 2)
    while next_locations:
        next_location = next_locations.pop()
        if visited[next_location] > visited[location]:
            visited[next_location] = visited[location]
            queue.append(next_location)
            # print(next_location, visited[next_location])


    if location > 0:
        next_locations.append(location - 1)
    if location < 100000:
        next_locations.append(location + 1)
    
    while next_locations:
        next_location = next_locations.pop()
        if visited[next_location] > visited[location] + 1:
            visited[next_location] = visited[location] + 1
            queue.append(next_location)
            # print(next_location, visited[next_location])

# print(visited[1:20])
print(time)