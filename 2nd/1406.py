import sys
from collections import deque

string1 = list(sys.stdin.readline().rstrip())
string2 = deque([])
n = int(sys.stdin.readline())
for _ in range(n):
    inputs = sys.stdin.readline().rstrip().split()

    if inputs[0] == 'P':
        string1.append(inputs[1])
    elif inputs[0] == 'L':
        if not string1:
            continue
        string2.appendleft(string1.pop())
    elif inputs[0] == 'D':
        if not string2:
            continue
        string1.append(string2.popleft())
    elif inputs[0] == 'B':
        if not string1:
            continue
        string1.pop()

result = string1 + list(string2)
print(''.join(result))