# 2670 : 연속부분최대곱
# https://www.acmicpc.net/problem/2670
import sys

n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    numbers.append(float(sys.stdin.readline()))
# print(numbers)

for i in range(1, n):
    numbers[i] = max(numbers[i], numbers[i-1] * numbers[i])
print('%0.3f' % max(numbers))