# 조합 문제
# N : 최대 100

# 1차 시도 : 제한시간 초과
# combinations 를 구하는 과정에서 시간 초과가 발생했다.

from itertools import combinations

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    scores = set(map(lambda x: int(x), input().split()))

    cases = set()
    combination_list = [0 for _ in range(n)] + list(scores)
    for temp in combinations(combination_list, len(scores)):
        cases.add(sum(temp))
    print(len(cases))