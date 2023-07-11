# https://www.acmicpc.net/problem/15652
import sys

def combination_with_replacement(cur, index):
    if len(cur) == m:
        print(*cur)
        return

    for i in range(index, n):
        combination_with_replacement(cur + [nums[i]], i)


n, m = map(lambda x: int(x), sys.stdin.readline().split())
nums = [i for i in range(1, n+1)]
combination_with_replacement([], 0)