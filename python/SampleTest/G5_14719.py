# https://www.acmicpc.net/problem/14719
import sys

height, width = map(lambda x: int(x), sys.stdin.readline().split())
block_heights = list(map(lambda x: int(x), sys.stdin.readline().split()))

maps = [[0 for _ in range(width)] for _ in range(height)]
for x in range(width):
    for y in range(block_heights[x]):
        maps[y][x] = 1

result = 0
for y in range(height):
    for x in range(width):
        # 블록인 곳은 체크하지 않음
        if maps[y][x] == 1:
            continue

        isLeft, isRight = False, False
        # 왼쪽 체크
        for left in range(0, x):
            if maps[y][left] == 1:
                isLeft = True
                break

        # 오른쪽 체크
        for right in range(x+1, width):
            if maps[y][right] == 1:
                isRight = True
                break

        if isLeft and isRight:
            result += 1
print(result)