# 17451 : 평행 우주
# https://www.acmicpc.net/problem/17451
import sys
import math

n = int(sys.stdin.readline())
planet_list = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))

for i in range(n-1, 0, -1):
    if planet_list[i-1] < planet_list[i]:
        planet_list[i-1] = math.ceil(planet_list[i]/planet_list[i-1]) * planet_list[i-1]

print(planet_list[0])