# https://www.acmicpc.net/problem/15665
import sys


def product(cur):
    global prev
    if len(cur) == m:
        print(*cur)
        return

    for i in range(n):
        if cur + [nums[i]] == prev:
            continue

        prev = cur + [nums[i]]
        product(cur + [nums[i]])
    prev = cur


n, m = map(lambda x: int(x), sys.stdin.readline().split())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
nums.sort()

prev = []
product([])