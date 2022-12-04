# 1049 : 기타줄
# https://www.acmicpc.net/problem/1049

N, M = map(lambda x: int(x), input().split(" "))

set_min = 10000000
single_min = 10000000
for i in range(0, M):
    package_cost, single_cost = map(lambda x: int(x), input().split(" "))
    set_min = min(set_min, package_cost)
    single_min = min(single_min, single_cost)

print(min(set_min * (N // 6 + 1), set_min * (N // 6) + single_min * (N % 6)))