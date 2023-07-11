# https://www.acmicpc.net/problem/15649
import sys


def permutation(cur, count):
    if count == m:
        print(*cur)
        return

    for i in range(n):
        if visited[i] == 1:
            continue

        visited[i] = 1
        permutation(cur + [nums[i]], count + 1)
        visited[i] = 0


n, m = map(lambda x: int(x), sys.stdin.readline().split())
visited = [0 for i in range(n)]
nums = [i for i in range(1, n+1)]
permutation([], 0)