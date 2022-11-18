# 5585 : 거스름돈
# https://www.acmicpc.net/problem/5585

# input : 내야할 돈
# 항상 1000원을 사용한다.
# output : 거스름 동전의 개수
# 동전의 종류는, 500 / 100 / 50 / 10 / 5 / 1

cost = int(input())
exchange = 1000 - cost
num_of_coins = 0

coin_list = [500, 100, 50, 10, 5, 1]

for coin in coin_list:
    num_of_coins += exchange // coin
    exchange = exchange % coin

print(num_of_coins)