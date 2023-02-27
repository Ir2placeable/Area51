# https://www.acmicpc.net/problem/12101

# 중복순열
import sys


def product(cur):
    if sum(cur) > n:
        return

    if sum(cur) == n:
        results.append(cur)
        return

    for i in range(3):
        product(cur + [nums[i]])


n, k = map(lambda x: int(x), sys.stdin.readline().split())
nums = [1, 2, 3]
results = []
product([])

if len(results) < k-1:
    print(-1)
else:
    print('+'.join(list(map(lambda x: str(x), results[k-1]))))