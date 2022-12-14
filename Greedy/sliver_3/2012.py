# 2012 : 등수 매기기
# https://www.acmicpc.net/problem/2012
import sys

n = int(sys.stdin.readline())
a = []
for _ in range(0, n):
    a.append(int(sys.stdin.readline()))
a.sort()

b = 0
for i in range(0, n):
    b += abs(i+1 - a[i])

print(b)
