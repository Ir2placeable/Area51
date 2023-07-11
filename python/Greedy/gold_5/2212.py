# 2212 : 센서
# https://www.acmicpc.net/problem/2212
import sys

sensors = int(sys.stdin.readline())
hubs = int(sys.stdin.readline())
sensor_list = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
sensor_list.sort()

diff = []
for i in range(0, sensors-1):
    diff.append(sensor_list[i+1] - sensor_list[i])
diff.sort()

coverage = 0
for i in range(0, len(diff) - (hubs-1)):
    coverage += diff[i]

print(coverage)