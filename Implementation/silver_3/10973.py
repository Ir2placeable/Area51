# https://www.acmicpc.net/problem/10973

import sys

n = int(sys.stdin.readline())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))

if nums == sorted(nums):
    print(-1)
else:
    out_flag = False
    for i in range(n-1, 0, -1):
        if out_flag:
            break
        if nums[i-1] > nums[i]:
            for j in range(n-1, 0, -1):
                if nums[i-1] > nums[j]:
                    nums[i-1], nums[j] = nums[j], nums[i-1]
                    nums = nums[:i] + sorted(nums[i:], reverse=True)

                    out_flag = True
                    break
    print(*nums)