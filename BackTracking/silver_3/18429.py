# https://www.acmicpc.net/problem/18429
import sys


def permutation(cur, day):
    global result

    if day == n:
        result += 1
        return

    if cur < 0:
        return

    for i in range(n):
        if used[i] == 1:
            continue

        used[i] = 1
        permutation(cur + nums[i] - k, day + 1)
        used[i] = 0


n, k = map(lambda x: int(x), sys.stdin.readline().split())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
used = [0 for _ in range(n)]

result = 0
permutation(0, 0)
print(result)