# 2491 : 수열
# https://www.acmicpc.net/problem/2491

# 9
# 4 1 3 3 2 2 9 2 3
import sys

n = int(sys.stdin.readline())
numbers = list(map(lambda x: int(x), sys.stdin.readline().split()))
# print(numbers)

index = 0
max_up, max_down = 0, 0
up, down = 0, 0
while index < n-1:
    if numbers[index] > numbers[index+1]:
        down += 1
        up = 0
    elif numbers[index] < numbers[index+1]:
        up += 1
        down = 0
    else:
        up += 1
        down += 1
    index += 1
    max_up = max(max_up, up)
    max_down = max(max_down, down)

print(max(max_up, max_down) + 1)