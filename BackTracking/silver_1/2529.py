# https://www.acmicpc.net/problem/2529
import sys


def permutation(cur, index):
    global min_val, max_val

    if index == n:
        val = ''
        for temp in cur:
            val += str(temp)

        min_val = min(min_val, val)
        max_val = max(max_val, val)
        return

    next_nums = []
    if items[index] == '>':
        next_nums = list(filter(lambda x: cur[-1] > x, nums))
    elif items[index] == '<':
        next_nums = list(filter(lambda x: cur[-1] < x, nums))

    for next_num in next_nums:
        if visited[next_num]:
            continue

        visited[next_num] = True
        permutation(cur + [next_num], index + 1)
        visited[next_num] = False


n = int(sys.stdin.readline())
items = list(sys.stdin.readline().split())
nums = [i for i in range(10)]

min_val, max_val = str(sys.maxsize), str(-sys.maxsize)
for start in range(10):
    visited = [False for i in range(10)]
    visited[start] = True
    permutation([start], 0)

print(max_val)
print(min_val)