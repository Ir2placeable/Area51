# https://www.acmicpc.net/problem/2304

import sys

n = int(sys.stdin.readline())
poles = [list(map(lambda x: int(x), sys.stdin.readline().split())) for _ in range(n)]
poles.sort(key=lambda x: x[0])

max_index = 0
max_height = 0
for i in range(n):
    if poles[i][1] > max_height:
        max_height = poles[i][1]
        max_index = i

result = max_height
prev = [0, 0]
for i in range(max_index):
    if poles[i][1] > prev[1]:
        result += abs(poles[i][0] - prev[0]) * prev[1]
        prev = poles[i]

result += abs(poles[max_index][0] - prev[0]) * prev[1]
prev = [0, 0]
for i in range(n-1, max_index, -1):
    if poles[i][1] > prev[1]:
        result += abs(poles[i][0] - prev[0]) * prev[1]
        prev = poles[i]
result += abs(poles[max_index][0] - prev[0]) * prev[1]
print(result)