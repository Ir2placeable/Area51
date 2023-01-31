# https://www.acmicpc.net/problem/1475

# 숫자 9는 6으로 체크한다.
from collections import defaultdict
import sys, math

numbers = defaultdict(int)
string = sys.stdin.readline().rstrip()
for char in string:
    if char == '9':
        char = '6'

    numbers[char] += 1
numbers['6'] = math.ceil(numbers['6']/2)
print(max(numbers.values()))