# 1448 : 삼각형 만들기
# https://www.acmicpc.net/problem/1448
import sys
# a < b + c
n = int(sys.stdin.readline())
item = []
for i in range(0, n):
    item.append(int(sys.stdin.readline()))
item.sort(reverse=True)

result = -1
for a in range(0, n-2):
    b = a + 1
    c = a + 2
    if item[a] < item[b] + item[c]:
        result = item[a] + item[b] + item[c]
        break

print(result)