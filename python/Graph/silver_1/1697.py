# 1697 : 숨바꼭질
# https://www.acmicpc.net/problem/1697
from collections import deque

n, k = map(lambda x: int(x), input().split(" "))

visited = [0 for _ in range(100001)]

queue = deque([n])
time = 0
while queue:
    location = queue.popleft()
    if location == k:
        time = visited[location]
        break

    time += 1
    next_locations = []
    if location > 0 :
        next_locations.append(location-1)
    if location < 100000:
        next_locations.append(location+1)
    if location*2 <= 100000:
        next_locations.append(2*location)
    for next_location in next_locations:
        if visited[next_location] == 0:
            visited[next_location] = visited[location] + 1
            queue.append(next_location)

print(time)