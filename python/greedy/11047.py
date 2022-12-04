# 11047 : 동전 0
# https://www.acmicpc.net/problem/11047

N, K = map(lambda x: int(x), input().split(" "))

coins = []
for i in range(0, N):
    coins.append(int(input()))

coins.sort(reverse=True)
need_coins = 0
for coin in coins:
    need_coins += K // coin
    K = K % coin

print(need_coins)