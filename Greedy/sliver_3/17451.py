# 17451 : 평행 우주
# https://www.acmicpc.net/problem/17451
import sys

n = int(sys.stdin.readline())
planet_list = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))

max_val = 0
max_idx = 0

for i in range(0, n):
    if planet_list[i] > max_val:
        max_val = planet_list[i]
        max_idx = i
# print(max_val, max_idx)

planet_list = planet_list[:max_idx+1]
planet_list.sort(reverse=True)
for i in range(1, len(planet_list)):
    temp = planet_list[i]
    while planet_list[i-1] > planet_list[i]:
        planet_list[i] += temp

print(planet_list[-1])