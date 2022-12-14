# 12018 : Yonsei ToTo
# https://www.acmicpc.net/problem/12018
import sys

n, m = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))

result = []
for i in range(0, n):
    a, b = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
    temp = list(map(lambda x: int(x), sys.stdin.readline().split(" ")))
    temp.sort()

    a = a - b
    if a < 0:
        result.append(1)
    else:
        result.append(temp[a])

result.sort()
count = 0
for i in range(0, n):
    if result[i] <= m:
        count += 1
        m -= result[i]
    else:
        break
print(count)