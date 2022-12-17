# 26215 : 눈 치우기
# https://www.acmicpc.net/problem/26215
import sys

n = int(sys.stdin.readline())
snow_list = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
snow_list.sort(reverse=True)

time = 0
while len(snow_list) > 1:
    a = snow_list.pop(0)
    b = snow_list.pop(0)
    time += b
    snow_list.append(a-b)
    snow_list.sort(reverse=True)

time += snow_list[0]
if time > 1440:
    time = -1
print(time)