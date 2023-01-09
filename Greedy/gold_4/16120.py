# 16120 : PPAP
# https://www.acmicpc.net/problem/16120
import sys
from collections import deque

string = sys.stdin.readline().rstrip()
items = deque([])
for char in string:
    items.append(char)
# print(items)

# items에 있는 요소를 모두 뽑는다.
stack = []
result = 'PPAP'
while items:
    # 앞에서 부터 뽑는다.
    item = items.popleft()

    if item == 'A':
        if len(stack) < 2:
            result = 'NP'
            break
        if len(items) == 0:
            result = 'NP'
            break
        if items[0] == 'A':
            result = 'NP'
            break
        # PPAP 달성
        stack.pop()
        stack.pop()
    elif item == 'P':
        stack.append(item)

print(result)