# https://www.acmicpc.net/problem/15656

import sys

def product(cur):
    if len(cur) == m:
        print(*cur)
        return

    for i in range(n):
        product(cur + [nums[i]])


n, m = map(lambda x: int(x), sys.stdin.readline().split())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
nums.sort()
product([])