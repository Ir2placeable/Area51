# 2720 : 세탁소 사장 동혁
# https://www.acmicpc.net/problem/2720

# 쿼터 : 0.25
# 다임 : 0.10
# 니켈 : 0.05
# 페니 : 0.01

num_of_cases = int(input())

for i in range(0, num_of_cases):
    target_exchange = int(input())

    quarter, dime, nickel, penny = 0, 0, 0, 0

    quarter = target_exchange // 25
    target_exchange = target_exchange % 25

    dime = target_exchange // 10
    target_exchange = target_exchange % 10

    nickel = target_exchange // 5
    penny = target_exchange % 5

    print(quarter, dime, nickel, penny)