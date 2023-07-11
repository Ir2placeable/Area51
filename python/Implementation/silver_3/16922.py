# https://www.acmicpc.net/problem/16922

import sys
from itertools import combinations_with_replacement

n = int(sys.stdin.readline())
numbers = [1, 5, 10, 50]

result = set()
for temp in combinations_with_replacement(numbers, n):
    result.add(sum(temp))
print(len(result))