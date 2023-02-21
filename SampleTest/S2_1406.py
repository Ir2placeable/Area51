# https://www.acmicpc.net/problem/1406
import sys
from collections import deque

string = list(sys.stdin.readline().rstrip())
queue = deque([])

n = int(sys.stdin.readline())
for _ in range(n):
    temp = sys.stdin.readline().split()

    if temp[0] == 'P':
        string.append(temp[1])
    elif temp[0] == 'L':
        if string:
            queue.appendleft(string.pop())
    elif temp[0] == 'D':
        if queue:
            string.append(queue.popleft())
    elif temp[0] == 'B':
        if string:
            string.pop()

print(''.join(string + list(queue)))