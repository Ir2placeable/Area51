# 1931 : 회의실 배정
# https://www.acmicpc.net/problem/1931

# 2초 / 128MB -> N^2 사용 가능한 것으로 예상됨
# 일단 회의실 일정을 정렬해서 봐야 할 필요가 있음.

# 1차 시도 : 회의실 스케줄을 시작시간으로 정렬한 뒤, 하나씩 시작으로 두고 계산해본다.
# 결과 : 시간 초과!
# import sys
#
# n = int(sys.stdin.readline())
#
# schedules = []
# for i in range(n):
#     schedules.append(list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))))
# schedules = sorted(schedules, key=lambda x: x[0])
# # print(schedules)
#
# max_slot = 0
# for i in range(n):
#     end_time = schedules[i][1]
#
#     temp_slot = 1
#     for j in range(i, n):
#         if end_time > schedules[j][0]:
#             continue
#
#         temp_slot += 1
#         end_time = schedules[j][1]
#     max_slot = max(max_slot, temp_slot)
#
# print(max_slot)

# 2차 시도 : 회의실 사용 시간이 적은 순으로 정렬해본다. 기간이 최소인 것부터 뽑는다.
# 결과 : 시간 초과!
# import sys
#
# n = int(sys.stdin.readline())
#
# schedules = []
# for i in range(n):
#     schedules.append(list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))))
# schedules = sorted(schedules, key=lambda x: x[1] - x[0])
#
# count = 0
# time_slot = []
# for schedule in schedules:
#     flag = True
#     temp_slot = []
#     for j in range(schedule[0], schedule[1]):
#         temp_slot.append(j)
#         if j in time_slot:
#             flag = False
#             break
#
#     if flag:
#         time_slot = time_slot + temp_slot
#         count += 1
#
# print(count)

# 3차 시도 : 종료 시간으로 정렬한다. 사실 이유는 떠오르지 않는데, 예전에 이렇게 푸는게 기억난다.
# 88% 에서 실패 -> 어떤 조건을 놓치고 있는 것 같다.
# 1 1 / 0 1 / 1 2 로 입력을 넣는 경우, 0 1이 먼저 정렬되지 않는 문제가 발생한다. -> 따라서 x[0] 으로 먼저 정렬 후, x[1]로 정렬한다.
import sys

n = int(sys.stdin.readline())

schedules = []
for i in range(n):
    a, b = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
    if a > b:
        a, b = b, a
    schedules.append([a, b])
schedules = sorted(schedules, key=lambda x: x[0])
schedules = sorted(schedules, key=lambda x: x[1])
# print(schedules)

time_slot = 0
end_time = 0
for schedule in schedules:
    if schedule[0] >= end_time:
        end_time = schedule[1]
        time_slot += 1

print(time_slot)