# 17615 : 볼 모으기
# https://www.acmicpc.net/problem/17615

# 어떤 색의 공을 선택할지 기준을 찾아야 함 -> 핵심!
# 맨 마지막 색의 공을 기준으로 선택해보자 -> 실패!
# 모아져있는 공이 최대인 색의 반대 색을 선택해보자 -> 실패!
# 공 개수가 작은 것을 선택해보자 -> 실패!
# 연속된 공을 하나로 줄여보자

import sys

n = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

balls = []
for i in string:
    balls.append(i)

new_balls = []
i = 0
while i < n:
    target = balls[i]
    new_balls.append(target)
    for j in range(i, n):
        if balls[i] == target:
            i += 1
        else:
            break

# print(balls)
# print(new_balls)

new_balls.pop()
a, b = 0, 0
for ball in new_balls:
    if ball == 'R':
        a += 1
    else:
        b += 1

print(min(a, b))