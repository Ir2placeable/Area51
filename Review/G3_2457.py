# 딱보면 그리디 문제이다.
# 강의실 문제와 유사하다. 그러나 차이점은 이어지도록 만드는 것이다.

# 꽃이 지는 기간을 기준으로 삼는다.
# 다음 꽃들 중, 꽃이 피는 기간이 가장 가까운 것을 기준으로 삼는다.
# 이때, 가장 오래필 수 있는 꽃을 선택해야 한다!!!

import sys

n = int(sys.stdin.readline())
flowers = []
for _ in range(n):
    a, b, c, d = map(lambda x: int(x), sys.stdin.readline().split())
    flowers.append([100 * a + b, 100 * c + d])
flowers.sort(reverse=True)
# print(flowers)

target = 301
next_target = 0
result = 0

# 기준이 1201 이상이면, 11월 30일 까지 피는 꽃이 있기 때문에 더이상 뽑지 않아도 된다.
while target < 1201:
    # 이어서 꽃을 필 수 있는지 체크하기 위한 플래그이다.
    picked = False
    # 정렬된 꽃에서, 꽃이 지는 기간(target) 전에 피는 꽃을 찾는다.
    while flowers and flowers[-1][0] <= target:
        # 그 중, 가장 오래 필 수 있는 꽃을 선택한다.
        next_target = max(next_target, flowers.pop()[1])
        picked = True

    # 이어서 피는 꽃이 없다.
    if not picked:
        result = 0
        break

    # 다음 기준 설정
    target = next_target
    result += 1

print(result)