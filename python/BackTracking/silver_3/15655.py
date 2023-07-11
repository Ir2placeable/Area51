# https://www.acmicpc.net/problem/15655

import sys

def combination(cur, index):
    if len(cur) == m:
        print(*cur)
        return

    for i in range(index, n):
        combination(cur + [nums[i]], i+1)


n, m = map(lambda x: int(x), sys.stdin.readline().split())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
nums.sort()
combination([], 0)