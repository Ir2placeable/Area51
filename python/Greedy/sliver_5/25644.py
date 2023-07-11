# 25644 : 최대 상승
# https://www.acmicpc.net/problem/25644

days = int(input())
stock_list = list(map(lambda x: int(x), input().split(" ")))

min_stock = 1000000000000
max_income = 0
for i in range(0, days):
    min_stock = min(min_stock, stock_list[i])
    max_income = max(max_income, stock_list[i]-min_stock)

print(max_income)