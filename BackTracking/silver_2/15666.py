# https://www.acmicpc.net/problem/15666
import sys


def combination_with_replacement(cur, depth):
    global prev

    if len(cur) == m:
        print(*cur)
        return

    for i in range(depth, n):
        if prev == cur + [nums[i]]:
            continue

        prev = cur + [nums[i]]
        combination_with_replacement(cur + [nums[i]], i)

    prev = cur


n, m = map(lambda x: int(x), sys.stdin.readline().split())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
nums.sort()

prev = []
combination_with_replacement([], 0)