# https://www.acmicpc.net/problem/10819

# 순서를 바꾼다 = 순열

import sys


def getResult(numbers):
    return_value = 0
    for i in range(n-1):
        return_value += abs(numbers[i] - numbers[i+1])
    return return_value


def permutation(cur):
    global result

    if len(cur) == n:
        result = max(result, getResult(cur))
        return

    for i in range(n):
        if visited[i] == 1:
            continue

        visited[i] = 1
        permutation(cur + [nums[i]])
        visited[i] = 0

n = int(sys.stdin.readline())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
visited = [0 for _ in range(n)]
result = 0
permutation([])
print(result)