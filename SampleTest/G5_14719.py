# https://www.acmicpc.net/problem/14719
import sys

# 그냥 이차원 배열 maps로 구현해서 각 위치를 탐색한다.
# 만약 특정 위치의 왼쪽과 오른쪽이 막혀있으면 +1 한다.

height, width = map(lambda x: int(x), sys.stdin.readline().split())
numbers = list(map(lambda x: int(x), sys.stdin.readline().split()))

maps = [[0 for _ in range(width)] for _ in range(height)]
for i in range(width):
    for j in range(numbers[i]):
        maps[j][i] = 1

result = 0
for y in range(height):
    for x in range(width):
        if maps[y][x] == 0:
            left, right = False, False

            for i in range(0, x):
                if maps[y][i] == 1:
                    left = True
                    break
            for i in range(x, width):
                if maps[y][i] == 1:
                    right = True
                    break
            if left and right:
                result += 1
print(result)