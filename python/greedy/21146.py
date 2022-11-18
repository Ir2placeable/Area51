# 21146 : Rating Problems
# https://www.acmicpc.net/problem/21146


num_of_judges, num_of_judged = map(lambda x: int(x), input().split(" "))

min_value, max_value = (num_of_judges-num_of_judged) * -3, (num_of_judges-num_of_judged) * 3

for i in range(0, num_of_judged):
    input_value = int(input())
    min_value += input_value
    max_value += input_value

print(min_value/num_of_judges, max_value/num_of_judges)

