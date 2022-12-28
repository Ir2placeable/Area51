# 4889 : 안정적인 문자열
# https://www.acmicpc.net/problem/4889

# 이런 문제 특징 : 그리디 + 스택 사용이다.
import sys

while True:
    string = sys.stdin.readline().rstrip()
    if string[0] == '-':
        break

    stack = []
    change = 0
    for char in string:
        if char == '{':
            stack.append(char)

        elif char == '}':
            if len(stack) > 0:
                stack.pop()
            else:
                change += 1
                stack.append('{')

    change += len(stack)//2

    print(change)