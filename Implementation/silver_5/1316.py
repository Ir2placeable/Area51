# https://www.acmicpc.net/problem/1316

import sys
n = int(sys.stdin.readline())


def checkGroupWord(string):
    stack = []
    isGroupWord = True
    for char in string:
        if not stack:
            stack.append(char)
            continue

        if char != stack[-1] and char in stack:
            isGroupWord = False
            break

        stack.append(char)
    return isGroupWord


result = 0
for _ in range(n):
    string = sys.stdin.readline().rstrip()

    if checkGroupWord(string):
        result += 1
print(result)