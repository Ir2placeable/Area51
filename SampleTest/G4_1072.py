# https://www.acmicpc.net/problem/1027
import sys


def getGradient(a, b):
    return (heights[a] - heights[b]) / (a - b)


n = int(sys.stdin.readline())
heights = list(map(lambda x: int(x), sys.stdin.readline().split()))

isVisible = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        gradient = getGradient(i, j)

        visible = 1
        for k in range(i + 1, j):
            temp_gradient = getGradient(i, k)
            if temp_gradient >= gradient:
                visible = 0
                break
        isVisible[i][j] = visible
        isVisible[j][i] = visible

result = 0
for temp in isVisible:
    result = max(result, sum(temp))
print(result)