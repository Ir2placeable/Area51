# https://www.acmicpc.net/problem/1253

# 두개의 수를 더한다는 것이 문제에 써있음 -> 투 포인터가 생각남
import sys

n = int(sys.stdin.readline())
nums = list(map(lambda x: int(x), sys.stdin.readline().split()))
nums.sort()

result = 0
for i in range(n):
    target_num = nums[i]
    left, right = 0, n-1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        left_num, right_num = nums[left], nums[right]
        if left_num + right_num > target_num:
            right -= 1
        elif left_num + right_num < target_num:
            left += 1
        else:
            result += 1
            break
print(result)