# https://www.acmicpc.net/problem/15663
import sys


def permutation(cur):
    global prev
    if len(cur) == m:
        print(*cur)
        return

    for i in range(n):
        if visited[i] == 1:
            continue
        if prev and prev[-1] == cur + [nums[i]]:
            continue

        visited[i] = 1
        prev.append(cur + [nums[i]])
        permutation(cur + [nums[i]])
        visited[i] = 0
    prev = [cur]


n, m = map(lambda x: int(x), sys.stdin.readline().split())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
nums.sort()

visited = [0 for _ in range(n)]
prev = []
permutation([])