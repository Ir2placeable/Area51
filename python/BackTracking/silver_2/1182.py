# https://www.acmicpc.net/problem/1182
import sys


def backTracking(cur, index):
    global result
    if sum(cur) == target and cur:
        result += 1

    for i in range(index, n):
        backTracking(cur + [nums[i]], i + 1)


n, target = map(lambda x: int(x), sys.stdin.readline().split())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
result = 0
backTracking([], 0)
print(result)