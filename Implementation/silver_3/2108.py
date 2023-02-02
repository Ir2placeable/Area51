# https://www.acmicpc.net/problem/2108

# 산술평균 : N개의 수들의 합을 N으로 나눈 값 -> sum / len
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값 -> sort
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값 -> dict
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이 -> sort

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(nums) / n))

# 중앙값
nums.sort()
print(nums[n//2])

# 최빈값
nums_dict = defaultdict(int)
for num in nums:
    nums_dict[num] += 1
# print('dict : ', nums_dict)
max_freq = max(nums_dict.values())
temp = list(filter(lambda x: x[1] == max_freq, nums_dict.items()))
temp.sort(key=lambda x: x[0])
if len(temp) > 1:
    print(temp[1][0])
else:
    print(temp[0][0])

# 범위
print(nums[-1] - nums[0])