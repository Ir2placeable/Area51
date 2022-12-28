# 1263 : 시간 관리
# https://www.acmicpc.net/problem/1263

# 소요시간 / 마감시간 순으로 들어온다.
import sys

n = int(sys.stdin.readline())
schedules = []

for i in range(n):
    a, b = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
    schedules.append([a, b])

schedules = sorted(schedules, key=lambda x: x[1], reverse=True)
# print(schedules)

cur_time = schedules[0][1]
for schedule in schedules:
    if cur_time > schedule[1]:
        cur_time = schedule[1]

    cur_time -= schedule[0]

    if cur_time < 0:
        cur_time = -1
        break

print(cur_time)