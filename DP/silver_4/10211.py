# 10211 : Maximum Subarray
# https://www.acmicpc.net/problem/10211
import sys

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n = int(sys.stdin.readline())
    numbers = list(map(lambda x: int(x), sys.stdin.readline().split()))

    for i in range(1, n):
        numbers[i] = max(numbers[i], numbers[i] + numbers[i-1])

    print(max(numbers))