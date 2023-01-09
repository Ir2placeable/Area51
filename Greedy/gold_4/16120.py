# 16120 : PPAP
# https://www.acmicpc.net/problem/16120
import sys
from collections import deque

string = sys.stdin.readline().rstrip()

stack = []
ace = 0
for char in string:
    if char == 'P' and ace == 0:
        stack.append(char)
    elif char == 'A':
        ace = 1
        stack.append(char)
    elif char == 'P' and ace == 1:
        ace = 0
        for _ in range(3):
            stack.pop()
        stack.append(char)
