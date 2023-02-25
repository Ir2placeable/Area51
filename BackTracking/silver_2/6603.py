# https://www.acmicpc.net/problem/6603
import sys


def combination(cur, index):
    if len(cur) == 6:
        print(*cur)
        return

    for i in range(index, n):
        combination(cur + [nums[i]], i + 1)


while True:
    temp = list(map(lambda x: int(x), sys.stdin.readline().split()))
    if temp[0] == 0:
        break

    n = temp[0]
    nums = temp[1:]
    combination([], 0)
    print()