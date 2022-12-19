# 11501 : 주식
# https://www.acmicpc.net/problem/11501

# 최대 값에 도달하기 전에는 하나씩 주식을 산다.
# 최대 값에 도달할 때 모든 주식을 판매한다.

test_case = int(input())

for i in range(0, test_case):
    days = int(input())
    costs = list(map(lambda x: int(x), input().split(" ")))

    max_value = costs[-1]
    margin = 0
    for j in range(days-1, -1, -1):
        if costs[j] < max_value:
            margin += max_value - costs[j]
        elif costs[j] > max_value:
            max_value = costs[j]

    print(margin)