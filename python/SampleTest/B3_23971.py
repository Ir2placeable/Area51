# https://www.acmicpc.net/problem/23971

# 그리디 + 구현 문제 같다.
# 0,0 부터 앉을 수 있다는 고정특징을 이용한다.

import sys

height, width, n, m = map(lambda x: int(x), sys.stdin.readline().split())

result = 0
max_y, max_x = 0, 0

index = 0
while index < height:
    max_y += 1
    index += n + 1

index = 0
while index < width:
    max_x += 1
    index += m + 1

result = max_y * max_x
print(result)