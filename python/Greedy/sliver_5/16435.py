# 16435 : 스네이크버드
# https://www.acmicpc.net/problem/16435

fruits, sb_height = map(lambda x: int(x), input().split(" "))
fruits_height = list(map(lambda x: int(x), input().split(" ")))
fruits_height.sort()

for fruit in fruits_height:
    if fruit <= sb_height:
        sb_height += 1

print(sb_height)