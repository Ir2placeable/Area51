# https://www.acmicpc.net/problem/2531
import sys

# 연속해서 k개를 체크하며 최대 초밥개수 카운팅 -> 시간초과

# 일반적인 답은 항상 k + 1 개 이다. (초밥이 항상 서로 다른 종류일 떄)
# 유별난 것은 초밥이 항상 같은 종류로 있는 경우이다.

dishes, sushies, inarow, coupon = map(lambda x: int(x), sys.stdin.readline().split())
belt = []
for _ in range(dishes):
    belt.append(int(sys.stdin.readline()))

result = 0
for left in range(dishes):
    temp = set()
    for i in range(left, left + inarow):
        i %= dishes
        temp.add(belt[i])

    if coupon in temp:
        result = max(result, len(temp))
    else:
        result = max(result, len(temp) + 1)

print(result)