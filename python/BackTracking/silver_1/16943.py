# https://www.acmicpc.net/problem/16943
import sys


def permutation(cur):
    global result

    if len(cur) == n:
        temp_result = int(''.join(cur))
        if temp_result < b:
            result = max(result, temp_result)
        return

    for i in range(n):
        if visited[i]:
            continue

        if not cur and nums[i] == '0':
            continue

        visited[i] = True
        permutation(cur + [nums[i]])
        visited[i] = False


a, b = sys.stdin.readline().split()
b = int(b)
nums = list(a)
n = len(nums)
visited = [False for _ in range(n)]

result = -1
permutation([])
print(result)