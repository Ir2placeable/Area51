# 17521 : Byte Coin
# https://www.acmicpc.net/problem/17521

days, money = map(lambda x: int(x), input().split(" "))

stock = []
for i in range(0, days):
    stock.append(int(input()))

bot = stock[0]
i = 0
while i < days-1:
    if stock[i] > stock[i+1]:
        bot = stock[i+1]
        i += 1
    else:
        j = i+1
        while j < days-1 and stock[j] <= stock[j+1]:
            j += 1
        top = stock[j]

        money = (money % bot) + top * (money // bot)
        i = j
print(money)