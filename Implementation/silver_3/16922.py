# https://www.acmicpc.net/problem/16922

from itertools import permutations
import sys

n = int(sys.stdin.readline())
base = [1, 5, 10, 50] * n

result = set()
for temp in permutations(base, n):
    result.add(sum(temp))
print(len(result))