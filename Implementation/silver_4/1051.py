# https://www.acmicpc.net/problem/1051

# n, m < 50 -> 완전 탐색 가능
import sys

height, width = map(lambda x: int(x), sys.stdin.readline().split())
nums = []
for _ in range(height):
    nums.append(list(sys.stdin.readline().rstrip()))

max_length = min(height, width)
result = 1
for k in range(1, max_length):
    for y in range(height-k):
        for x in range(width-k):
            a = nums[y][x]
            b = nums[y][x+k]
            c = nums[y+k][x]
            d = nums[y+k][x+k]

            if a == b == c == d:
                result = (k+1) ** 2
print(result)