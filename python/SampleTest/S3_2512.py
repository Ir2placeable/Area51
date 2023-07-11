# https://www.acmicpc.net/problem/2512
import sys

n = int(sys.stdin.readline())
budgets = list(map(lambda x: int(x), sys.stdin.readline().split()))
total = int(sys.stdin.readline())

left, right = 0, max(budgets)

while left <= right:
    mid = (left + right) // 2

    temp_total = sum(list(map(lambda x: min(mid, x), budgets)))
    if temp_total > total:
        right = mid - 1
    else:
        left = mid + 1

print(right)