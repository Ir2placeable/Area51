# 2812 : 크게 만들기
# https://www.acmicpc.net/problem/2812
import sys

# 규칙1 : 앞자리 수가 뒷자리 수 보다 작을 때 뺀다.
# 규칙2 : 규칙1 을 수행한 후 처음부터 다시 시작한다.

n, k = map(lambda x: int(x), sys.stdin.readline().split())
string = sys.stdin.readline().rstrip()

stack = []
for char in string:
    while stack and stack[-1] < char and k > 0:
        stack.pop()
        k -= 1
    stack.append(char)
result = ''
for num in stack:
    result += num
print(result[:n-k])