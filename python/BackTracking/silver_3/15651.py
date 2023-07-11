# https://www.acmicpc.net/problem/15651
import sys


def product(cur):
    if len(cur) == m:
        print(*cur)
        return

    for i in range(n):
        product(cur + [nums[i]])


n, m = map(lambda x: int(x), sys.stdin.readline().split())
nums = [i for i in range(1, n+1)]
product([])