# 25496 : 장신구 명장 임스
# https://www.acmicpc.net/problem/25496

P, N = map(lambda ele: int(ele), input().split(" "))

maker_list = list(map(lambda ele: int(ele), input().split(" ")))
maker_list.sort()

P = 200 - P
accessories = 0
for item in maker_list:
    if P <= 0:
        break
    P -= item
    accessories += 1

print(accessories)