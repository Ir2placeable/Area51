# https://www.acmicpc.net/problem/2512

# 예산의 최대 크기가 크다 -> 브루트포스 불가능
# 지방의 최대 크기가 10000 이다 -> 이분탐색

import sys

n = int(sys.stdin.readline())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
total = int(sys.stdin.readline())
nums.sort()

if sum(nums) < total:
    print(max(nums))
elif nums[0] * n > total:
    print(total // n)
else:
    left, right = 0, 0
    for i in range(n-1):
        temp = sum(nums[:i]) + nums[i] * (n - i)
        if temp > total:
            left, right = nums[i-1], nums[i]
            break

    mid = (left + right) // 2
    prev = 0
    temp = sum(list(map(lambda x: min(x, mid), nums)))
    while prev != temp:
        if temp < total:
            left = mid
        elif temp > total:
            right = mid
        mid = (left + right) // 2

        prev = temp
        temp = sum(list(map(lambda x: min(x, mid), nums)))
    print(mid)