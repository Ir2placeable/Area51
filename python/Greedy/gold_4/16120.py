# 16120 : PPAP
# https://www.acmicpc.net/problem/16120
import sys

string = sys.stdin.readline().rstrip()

stack = []
ace = 0
for char in string:
    if len(stack) > 3:
        if stack[-4:] == ['P', 'P', 'A', 'P']:
            for _ in range(4):
                stack.pop()
            stack.append('P')
    stack.append(char)

if stack == ['P'] or stack == ['P', 'P', 'A', 'P']:
    print('PPAP')
else:
    print('NP')