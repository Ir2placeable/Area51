# https://www.acmicpc.net/problem/19637

# 메모리 제한이 큼 -> 메모리를 이용하는 문제이다.
import sys

n, m = map(lambda x: int(x), sys.stdin.readline().split())
conditions = []
for _ in range(n):
    a, b = sys.stdin.readline().split()
    conditions.append([int(b), a])

for _ in range(m):
    target = int(sys.stdin.readline())
    left = 0
    right = n-1
    mid = (left + right) // 2

    while left < right:
        if target <= conditions[mid][0]:
            right = mid
        else:
            left = mid + 1

        mid = (right + left) // 2

    print(conditions[mid][1])