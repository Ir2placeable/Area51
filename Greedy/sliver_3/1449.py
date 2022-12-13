# 1449 : 수리공 항승
# https://www.acmicpc.net/problem/1449

n, tape = map(lambda x: int(x), input().split(" "))
coverage = tape - 1
broken = list(map(lambda x: int(x), input().split(" ")))
broken.sort()

index = 0
need_tapes = 0
while index < n:
    need_tapes += 1
    j = index
    while j < n and broken[j] - broken[index] <= coverage:
        j += 1
    index = j

print(need_tapes)