# 1744 : 수 묶기
# https://www.acmicpc.net/problem/1744

# 음수는 묶어야 양수가 되기 때문에 -> 가능한 많이 묶는다.
# 음수의 수가 홀수인 경우, 묶어도 하나가 남는다. -> 0과 묶어서 제거한다.
# 양수는 묶어야 양수가 되기 때문에 -> 가능한 많이 묶는다.
# 1은 묶으면 손해이기 때문에 -> 1끼리 더한다.

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
numbers.sort()
# print(numbers)

under0 = []
over0 = []
zero = False
one = 0
for number in numbers:
    if number < 0:
        under0.append(number)
    elif number == 0:
        zero = True
    elif number == 1:
        one += 1
    else:
        over0.append(number)
# print(under0, zero, one, over0)

result = 0

# 2보다 큰 수들은 전부 곱한다.
over_index = len(over0) - 1
while over_index > -1:
    if over_index - 1 > -1:
        result += over0[over_index] * over0[over_index - 1]
        over_index -= 2
    else:
        result += over0[over_index]
        over_index -= 1

# print(result)
# 1은 전부 더한다.
result += one

# 0이 있는 경우
if zero:
    # 음수가 홀수인 경우 하나 제거한다.
    if len(under0) % 2 == 1:
        under0.pop()

under_index = 0
while under_index < len(under0):
    if under_index + 1 < len(under0):
        result += under0[under_index] * under0[under_index + 1]
        under_index += 2
    else:
        result += under0[under_index]
        under_index += 1

print(result)
