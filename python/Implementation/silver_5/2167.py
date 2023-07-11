# https://www.acmicpc.net/problem/2167

import sys
height, width = map(lambda x: int(x), sys.stdin.readline().split())
nums = [[0 for _ in range(width+1)] for _ in range(height+1)]
for y in range(1, height+1):
    temp = list(map(lambda x: int(x), sys.stdin.readline().split()))
    for x in range(width):
        nums[y][x+1] = temp[x] + nums[y][x]

k = int(sys.stdin.readline())
for _ in range(k):
    a, b, c, d = map(lambda x: int(x), sys.stdin.readline().split())

    result = 0
    for y in range(a, c+1):
        result += nums[y][d] - nums[y][b-1]
    print(result)