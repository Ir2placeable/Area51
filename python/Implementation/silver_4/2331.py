# https://www.acmicpc.net/problem/2331

import sys
from collections import defaultdict

n, k = map(lambda x: int(x), sys.stdin.readline().split())

d = defaultdict(int)
d[n] = 1
prev_number = n

while True:
    next_number = 0
    for num in str(prev_number):
        next_number += int(num) ** k

    if d[next_number] == 3:
        break
    d[next_number] += 1
    prev_number = next_number
    n -= 1

result = 0
for temp in d.values():
    if temp == 1:
        result += 1
print(result)