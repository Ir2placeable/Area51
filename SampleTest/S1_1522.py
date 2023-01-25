# https://www.acmicpc.net/problem/1522

# 연속된 b의 개수가 가장 긴 것을 찾는다.
# 거기에서 left, right로 뻡
import sys

string = list(sys.stdin.readline().rstrip())
print(string)
left = string.index('b')
right = len(string)-1

count = 0
while left < right:
    if string[right] == 'a':
        right -= 1
        continue
