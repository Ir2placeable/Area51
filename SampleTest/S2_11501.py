# https://www.acmicpc.net/problem/11501
import sys

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n = int(sys.stdin.readline())
    nums = list(map(lambda x: int(x), sys.stdin.readline().split()))

    result = 0
    max_num = 0
    while nums:
        current_num = nums.pop()

        if current_num > max_num:
            max_num = current_num

        else:
            result += max_num - current_num

    print(result)