# https://www.acmicpc.net/problem/7570

# 순서대로 서 있는 아이의 개수를 구하는 것이 관건이다.

# 5 2 4 1 3
# 2 - 3
# 1 - 3
# 최대 2명의 아이가 제대로 서 있다. -> 즉, 3명의 아이는 재배치 해야한다는 의미이다.

# 6 1 2 5 3 4
# 1 2 .. 3 4 -> 4명이 제대로 서 있다. -> 2명만 배치하면 끝이다.

import sys
n = int(sys.stdin.readline())
nums = [0] + list(map(lambda x: int(x), sys.stdin.readline().split()))

positions = [0 for i in range(n+1)]
for i in range(n+1):
    positions[nums[i]] = i

max_count = 0
count = 1
for i in range(1, n):
    if positions[i] < positions[i+1]:
        count += 1
    else:
        count = 1
    max_count = max(max_count, count)
print(n - max_count)