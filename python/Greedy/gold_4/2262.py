# 2262 : 토너먼트 만들기
# https://www.acmicpc.net/problem/2262

# 두 수의 차이의 합을 구하는 문제이다.
# 숫자를 어떻게 묶을 것 인가를 알아내는 것이 핵심이다.
# 큰 수 먼저 인접한 수를 중에 차이가 적은 수끼리 묶는다.

import sys

n = int(sys.stdin.readline())
numbers = list(map(lambda x: int(x), sys.stdin.readline().split()))

result = 0

for target_number in range(n, 1, -1):
    index_of_target = numbers.index(target_number)

    left, right = -1 * sys.maxsize, sys.maxsize
    if index_of_target > 0:
        left = numbers[index_of_target - 1]
    if index_of_target < len(numbers)-1:
        right = numbers[index_of_target + 1]

    numbers.pop(index_of_target)
    result += min(abs(target_number - left), abs(right - target_number))

print(result)