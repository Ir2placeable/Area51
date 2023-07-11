# https://www.acmicpc.net/problem/15664
import sys


def combination(cur, depth):
    global prev

    if len(cur) == m:
        print(*cur)
        return

    for i in range(depth, n):
        if prev == cur + [nums[i]]:
            continue

        prev = cur + [nums[i]]
        combination(cur + [nums[i]], i+1)

    prev = cur


n, m = map(lambda x: int(x), sys.stdin.readline().split())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
nums.sort()

prev = []
combination([], 0)