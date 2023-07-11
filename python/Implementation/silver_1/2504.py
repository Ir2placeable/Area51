# https://www.acmicpc.net/problem/2504

# 스택을 사용하는 문제이다.
# 스택에서 괄호를 제거할 때마다 점수가 계산된다.

# 점수 계산 과정이 다소 복잡한데, 곱셈의 교환법칙을 생각해야 한다.
# ( () [[]] ) => 2 * (2 + 3*3) = 2*2 + 2*3*3
# 괄호가 닫히면 결과값에 임시값을 저장한다. 이때, 교환법칙을 고려하여 나누기 2 or 3을 해주는 것이 관건이다.

import sys

brackets = list(sys.stdin.readline().rstrip())

result = 0
temp = 1
stack = []

for i in range(len(brackets)):
    if brackets[i] == '(':
        temp *= 2
        stack.append(brackets[i])
    elif brackets[i] == '[':
        temp *= 3
        stack.append(brackets[i])
    elif brackets[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break

        if brackets[i-1] == '(':
            result += temp
        stack.pop()
        temp //= 2
    elif brackets[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break

        if brackets[i-1] == '[':
            result += temp
        stack.pop()
        temp //= 3

if stack:
    result = 0

print(result)