# https://www.acmicpc.net/problem/2563

# 전체크기 100 * 100 = 10000 이다. 완전탐색이 가능하다.
import sys

maps = [[0 for _ in range(100)] for _ in range(100)]
n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(lambda x: int(x), sys.stdin.readline().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            maps[i][j] = 1

result = 0
for temp in maps:
    result += sum(temp)
print(result)