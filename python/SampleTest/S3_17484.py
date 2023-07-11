# https://www.acmicpc.net/problem/17484
import sys

height, width = map(lambda x: int(x), sys.stdin.readline().split())
maps = []
for i in range(height):
    maps.append(list(map(lambda x: int(x), sys.stdin.readline().split())))

dp = [[[sys.maxsize, sys.maxsize, sys.maxsize] for _ in range(width)] for _ in range(height + 1)]
dp[0] = [[0, 0, 0] for _ in range(width)]
for y in range(1, height + 1):
    for x in range(width):
        if x < width - 1:
            dp[y][x][0] = min(dp[y-1][x+1][1], dp[y-1][x+1][2]) + maps[y-1][x]
        if x > 0:
            dp[y][x][2] = min(dp[y-1][x-1][0], dp[y-1][x-1][1]) + maps[y-1][x]

        dp[y][x][1] = min(dp[y-1][x][0], dp[y-1][x][2]) + maps[y-1][x]
result = sys.maxsize
for temp in dp[-1]:
    result = min(result, min(temp))
print(result)