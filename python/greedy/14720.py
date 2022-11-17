# 14720 : 우유 축제
# https://www.acmicpc.net/problem/14720

# 딸기우유 : 0
# 초코우유 : 1
# 바나나우유 : 2

# 우유 가게 갯수
num_of_stores = int(input())

stores_list = list(map(lambda ele: int(ele), input().split(" ")))

# 영학이가 마셔야 하는 우유의 번호
target_milk = 0

# 영학이가 마신 우유의 횟수
drank_milks = 0

for milk_index in stores_list:
    if milk_index == target_milk:
        drank_milks += 1
        target_milk = (target_milk + 1) % 3

print(drank_milks)