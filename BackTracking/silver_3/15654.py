# https://www.acmicpc.net/problem/15654
import sys


def permutation(cur):
    if len(cur) == m:
        print(*cur)
        return

    for i in range(n):
        if visited[i] == 1:
            continue

        visited[i] = 1
        permutation(cur + [nums[i]])
        visited[i] = 0


n, m = map(lambda x: int(x), sys.stdin.readline().split())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
nums.sort()
visited = [0 for _ in range(n)]
permutation([])