# 2457 : 공주님의 정원
# https://www.acmicpc.net/problem/2457
import sys

# 1. 정렬하기 위해, 꽃이 피고 지는 날짜를 단일 수로 표현한다.
# 2. 꽃이 지는 날짜를 기준으로 삼고, 그 중 꽃이 가장 늦게 피는 꽃을 선택한다.

# 1 : 꽃을 단일 수로 표현
n = int(sys.stdin.readline())
flowers = []
for _ in range(n):
    a, b, c, d = map(lambda x: int(x), sys.stdin.readline().split())
    start_date, end_date = a * 100 + b, c * 100 + d
    flowers.append([start_date, end_date])
flowers.sort(key=lambda x: (x[0], x[1]))

count = 0
criteria = 301
next_criteria = 0
while flowers:
    # 꽃이 이어서 피지 못하는 경우
    if flowers[0][0] > criteria or criteria >= 1201:
        count = 0
        break

    for _ in range(len(flowers)):
        if flowers[0][0] <= criteria:
            if next_criteria <= flowers[0][1]:
                next_criteria = flowers[0][1]
            flowers.pop(0)
        else:
            break

    count += 1
    criteria = next_criteria

    if criteria >= 1201:
        break

if criteria < 1201:
    count = 0
print(count)