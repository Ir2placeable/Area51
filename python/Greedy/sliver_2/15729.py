# 15729 : 방탈출
# https://www.acmicpc.net/problem/15729
import sys

n = int(sys.stdin.readline())
lights = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))

moves = 0
for i in range(0, n):
    if lights[i] == 1:
        moves += 1
        j = i
        while j < n and j < i+3:
            lights[j] = (lights[j] + 1) % 2
            j += 1

print(moves)