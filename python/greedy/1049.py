# 1049 : 기타줄
# https://www.acmicpc.net/problem/1049

need_strings, brands = map(lambda x: int(x), input().split(" "))

min_package_cost, min_single_cost = 100000000000, 100000000000
for i in range(0, brands):
    package_cost, single_cost = map(lambda x: int(x), input().split(" "))

    min_package_cost = min(min_package_cost, package_cost)
    min_single_cost = min(min_single_cost, single_cost)
# print(min_package_cost, min_single_cost)

total_cost = 0
while need_strings > 0:
    if min_package_cost < min_single_cost * min(6, need_strings):
        total_cost += min_package_cost
        need_strings -= 6
    else:
        total_cost += min_single_cost
        need_strings -= 1

print(total_cost)