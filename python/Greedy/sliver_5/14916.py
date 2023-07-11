# 14916 : 거스름돈
# https://www.acmicpc.net/problem/14916

# 거스름돈 동전의 최소 개수?
# 종류 : 2 / 5

coins = 0
exchange = int(input())

while exchange % 5 != 0 and exchange > 0:
    coins += 1
    exchange -= 2

if exchange < 0 :
    print(-1)
else:
    coins += exchange // 5
    print(coins)