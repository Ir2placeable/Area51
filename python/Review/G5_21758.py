# 특정 시작점에서 특정 종료점까지 의 누적합을 구해야한다. 이때, 누적합이 최대가 되어야한다. -> 그리디 문제
# 특정 시작점과 특정 종료점은 임의의 점이다. -> 케이스를 나누어야 한다.
# 케이스를 어떻게 나눌지 고민하는 과정이 제법 어려운데, 천천히 생각해보면 다음과 같다.
# 누적합이 최대가 되어야 한다. 즉, 쭉 쓸고 가야한다. 꿀통 이전까지의 꿀을 전부 쓸어야 하기 때문에, 꿀통과 벌은 서로 반대편에 위치해야 한다.
    # case 1 : 벌 벌 .... 꿀통
    # case 2 : 꿀통 .... 벌 벌
# 벌이 시작한 위치에서는 누적합을 더할 수 없다. 만약 벌이 시작한 위치의 꿀이 존나게 크다. 여기는 무조건 먹어야 한다.
    # 첫번째 위치의 꿀은 무슨 수를 해도 먹을 수 없다.
    # 두번째 위치의 꿀은 두번째 벌의 위치를 옮기면 먹을 수 있다.
    # 즉, 첫번째 벌의 위치는 고정이고 두번째 벌의 위치는 꿀통 전까지 움직일 수 있다.
# 꿀통이 중간에 위치하는 경우도 존재한다. 이때, 벌은 양 사이드 끝으로 고정된다. 꿀을 전부 쓸어야 하기 때문이다.
    # case 3 : 벌 ... 꿀통 ... 벌

import sys

n = int(sys.stdin.readline())
honeys = list(map(lambda x: int(x), sys.stdin.readline().split()))
result = 0

# case 1 : 벌 벌 .... 꿀통
bee1 = sum(honeys[1:])
for i in range(1, n-1):
    bee2 = sum(honeys[i+1:])
    result = max(result, bee1 + bee2 - honeys[i])

# case 2 : 꿀통 .... 벌 벌
bee1 = sum(honeys[:n-1])
for i in range(1, n-1):
    bee2 = sum(honeys[:i])
    result = max(result, bee1 + bee2 - honeys[i])

# case 3 : 벌 ... 꿀통 ... 벌
temp = sum(honeys) - honeys[0] - honeys[-1]
for i in range(1, n-1):
    result = max(result, temp + honeys[i])
print(result)