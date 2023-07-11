# https://www.acmicpc.net/problem/2961
import sys


def combination(sour, bitter, index):
    global result

    if index > 0:
        result = min(result, abs(sour - bitter))

    for i in range(index, n):
        combination(sour * ingredients[i][0], bitter + ingredients[i][1], i + 1)


n = int(sys.stdin.readline())
ingredients = [list(map(lambda x: int(x), sys.stdin.readline().split())) for _ in range(n)]
result = sys.maxsize

combination(1, 0, 0)
print(result)