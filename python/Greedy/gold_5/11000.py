# 11000 : 강의실 배정
# https://www.acmicpc.net/problem/11000
import sys
import heapq

n = int(sys.stdin.readline())
schedules = []
for i in range(n):
    temp = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
    schedules.append(temp)

schedules.sort()
# rooms : priority queue
# sort() 함수는 O(N logN) 임 -> 여기서 시간 초과 발생. -> heapq를 사용해야 한다!
# heappush(), heappop() 함수는 O(log N)임
# 앞으로 우선순위큐는 heapq를 사용하자!
rooms = []
for schedule in schedules:
    if len(rooms) == 0:
        heapq.heappush(rooms, schedule[1])
    elif schedule[0] < rooms[0]:
        heapq.heappush(rooms, schedule[1])
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, schedule[1])

print(len(rooms))
