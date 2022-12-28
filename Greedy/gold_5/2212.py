# 2212 : 센서
# https://www.acmicpc.net/problem/2212
import math
import sys

sensors = int(sys.stdin.readline())
hubs = int(sys.stdin.readline())
sensor_list = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
sensor_list.sort()
print(sensor_list)