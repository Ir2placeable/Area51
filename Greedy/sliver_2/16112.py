# 16112 : 5차 전직
# https://www.acmicpc.net/problem/16112

n, k = map(lambda x: int(x), input().split(" "))
stones = list(map(lambda x: int(x), input().split(" ")))
stones.sort()

total_exp = 0
on = 0
for stone in stones:
    total_exp += stone * min(on, k)
    on += 1

print(total_exp)