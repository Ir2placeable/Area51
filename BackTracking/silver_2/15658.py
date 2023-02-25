# https://www.acmicpc.net/problem/15658
import sys


def backTracking(cur, index):
    global min_val, max_val

    if index == n:
        max_val = max(max_val, cur)
        min_val = min(min_val, cur)
        return

    if operators[0] > 0:
        operators[0] -= 1
        backTracking(cur + nums[index], index + 1)
        operators[0] += 1
    if operators[1] > 0:
        operators[1] -= 1
        backTracking(cur - nums[index], index + 1)
        operators[1] += 1
    if operators[2] > 0:
        operators[2] -= 1
        backTracking(cur * nums[index], index + 1)
        operators[2] += 1
    if operators[3] > 0:
        operators[3] -= 1
        backTracking(int(cur / nums[index]), index + 1)
        operators[3] += 1


n = int(sys.stdin.readline())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
operators = list(map(lambda x: int(x), sys.stdin.readline().split()))

max_val, min_val = -sys.maxsize, sys.maxsize
backTracking(nums[0], 1)
print(max_val)
print(min_val)