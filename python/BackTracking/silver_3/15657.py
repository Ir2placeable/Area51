# https://www.acmicpc.net/problem/15657
import sys


def combination_with_replacement(cur, index):
    if len(cur) == m:
        print(*cur)
        return

    for i in range(index, n):
        combination_with_replacement(cur + [nums[i]], i)


n, m = map(lambda x: int(x), sys.stdin.readline().split())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
nums.sort()
combination_with_replacement([], 0)