# https://www.acmicpc.net/problem/11866

import sys
from collections import deque
n, k = map(lambda x: int(x), sys.stdin.readline().split())

people = deque([i for i in range(1, n+1)])
result = []

while people:
    for i in range(k):
        people.append(people.popleft())
    result.append(people.pop())

temp = '<'
for i in range(n-1):
    temp += str(result[i]) + ', '
temp += str(result[-1]) + '>'
print(temp)