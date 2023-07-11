# 1374 : 강의실
# https://www.acmicpc.net/problem/1374
import sys
import heapq

n = int(sys.stdin.readline())

schedules = []
for _ in range(n):
    a, b, c = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
    schedules.append([b, c])
schedules = sorted(schedules, key=lambda x: x[0])
# print(schedules)

rooms = [0]
for schedule in schedules:
    start_time = schedule[0]
    end_time = schedule[1]
    # print(rooms, start_time, end_time)

    if rooms[0] <= start_time:
        heapq.heappop(rooms)
        heapq.heappush(rooms, end_time)
    else:
        heapq.heappush(rooms, end_time)
print(len(rooms))
