# https://www.acmicpc.net/problem/17615

# 공을 왼쪽으로 몰 수도 있고 오른쪽으로 몰 수도 있다.
# 초기값은 공이 적은 것을 옮기는 경우로 세팅한다.

import sys

n = int(sys.stdin.readline())
balls = list(sys.stdin.readline().rstrip())

result = 0
reds, blues = balls.count('R'), balls.count('B')
result = min(reds, blues)

left = 0
count = 0
while left < n and balls[0] == balls[left]:
    left += 1
    count += 1
if balls[0] == 'R':
    result = min(result, reds-count)
else:
    result = min(result, blues-count)

right = n-1
count = 0
while right > -1 and balls[-1] == balls[right]:
    right -= 1
    count += 1
if balls[-1] == 'R':
    result = min(result, reds-count)
else:
    result = min(result, blues-count)

print(result)