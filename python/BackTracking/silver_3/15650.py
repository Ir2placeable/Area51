# https://www.acmicpc.net/problem/15650
import sys


def combination(cur, count):
    if len(cur) == m:
        print(*cur)
        return

    for i in range(count, n):
        combination(cur + [nums[i]], i + 1)


n, m = map(lambda x: int(x), sys.stdin.readline().split())
nums = [i for i in range(1, n+1)]
combination([], 0)
