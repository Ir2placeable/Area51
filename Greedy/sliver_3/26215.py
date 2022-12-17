# 26215 : 눈 치우기
# https://www.acmicpc.net/problem/26215
import sys

n = int(sys.stdin.readline())

snow_list = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
snow_list.sort(reverse=True)

max_time = 1440
time = 0
while len(snow_list) > 1:
    temp_time = snow_list.pop()
    time += temp_time
    snow_list[0] -= temp_time

    if time > max_time:
        time = -1
        break

time += snow_list[0]
if time > max_time:
    time = -1
print(time)