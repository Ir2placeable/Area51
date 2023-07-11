# https://www.acmicpc.net/problem/2960

import sys
n, k = map(lambda x: int(x), sys.stdin.readline().split())

result = 0
nums = [i for i in range(2, n+1)]

while True:
    target = nums[0]

    index = 0
    while index < len(nums) and k > 0:
        if nums[index] % target == 0:
            result = nums[index]
            nums.remove(nums[index])
            k -= 1
        else:
            index += 1
    if k == 0:
        break
print(result)