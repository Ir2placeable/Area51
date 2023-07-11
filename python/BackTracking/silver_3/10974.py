# https://www.acmicpc.net/problem/10974
import sys


def permutation(cur):
    if len(cur) == n:
        print(*cur)
        return

    for i in range(n):
        if visited[i] == 1:
            continue

        visited[i] = 1
        permutation(cur + [nums[i]])
        visited[i] = 0


n = int(sys.stdin.readline())
nums = [i for i in range(1, n+1)]
visited = [0 for i in range(n)]
permutation([])