# https://www.acmicpc.net/problem/2110
import sys

n, target_APs = map(lambda x: int(x), sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()

min_diff = 1
max_diff = nums[-1] - nums[0]
result = 0

while min_diff <= max_diff:
    mid_diff = (min_diff + max_diff) // 2
    current_AP = nums[0]
    installed_APs = 1

    for i in range(1, n):
        if current_AP + mid_diff <= nums[i]:
            installed_APs += 1
            current_AP = nums[i]

    if installed_APs >= target_APs:
        min_diff = mid_diff + 1
        result = mid_diff
    else:
        max_diff = mid_diff - 1
print(result)