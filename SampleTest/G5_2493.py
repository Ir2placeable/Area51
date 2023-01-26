# https://www.acmicpc.net/problem/2493

# 송신기의 높이차를 따로 저장한다.
# 0번째 송신기는 항상 값이 0 이다.
# 0번째 송신기 높이를 기준으로 위, 아래가 생성된다.
#

import sys

n = int(sys.stdin.readline())
towers = list(map(lambda x: int(x), sys.stdin.readline().split()))
result = [0 for _ in range(n)]

# 0 : height / 1 : index
base = []
for i in range(0, n):
    while base and base[-1][0] < towers[i]:
        base.pop()

    temp_result = 0
    if base:
        temp_result = base[-1][1] + 1
    result[i] = temp_result
    base.append([towers[i], i])

if result[-1] == 0:
    print(0)
else:
    print(*result)