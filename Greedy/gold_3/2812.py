# 2812 : 크게 만들기
# https://www.acmicpc.net/problem/2812
import sys

# 규칙1 : 앞자리 수가 뒷자리 수 보다 작을 때 뺀다.
# 규칙2 : 규칙1 을 수행한 후 처음부터 다시 시작한다.

n, k = map(int, sys.stdin.readline().split())
string = list(sys.stdin.readline().strip())
# print(string)

stack = []
for char in string:
    while stack and k > 0 and stack[-1] < char:
        stack.pop()
        k -= 1
    stack.append(char)
result = ''
for i in range(len(stack)-k):
    result += stack[i]
print(result)