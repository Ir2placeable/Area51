# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

# 최댓값을 만들기 위해서는 큰 수를 곱해야 한다.
# 최소값을 만들기 위해서는 음수를 곱해야 한다.
# 결론적으로 맨 마지막 자리에는 곱하기가 들어와야 한다.

# 2
# 5 6
# 0 0 1 0

import sys

n = int(sys.stdin.readline())
numbers = list(map(lambda x: int(x), sys.stdin.readline().split()))
operator = list(map(lambda x: int(x), sys.stdin.readline().split()))
# operator = [ + - * / ]


def getMaxValue(numbers_copy, operator_copy):
    while len(numbers_copy) > 1:
        number1 = numbers_copy.pop(0)
        number2 = numbers_copy.pop(0)
        result = 0

        if operator_copy[1] > 0:
            result = number1 - number2
            operator_copy[1] -= 1
        elif operator_copy[3] > 0:
            result = number1 // number2
            operator_copy[3] -= 1
        elif operator_copy[0] > 0:
            result = number1 + number2
            operator_copy[0] -= 1
        elif operator_copy[2] > 0:
            result = number1 * number2
            operator_copy[2] -= 1

        numbers_copy.insert(0, result)
    return numbers_copy[0]

def getMinValue(numbers_copy, operator_copy):
    while len(numbers_copy) > 1:
        number1 = numbers_copy.pop(0)
        number2 = numbers_copy.pop(0)
        result = 0

        if operator_copy[0] > 0:
            result = number1 + number2
            operator_copy[0] -= 1
        elif operator_copy[3] > 0:
            result = number1 // number2
            operator_copy[3] -= 1
        elif operator_copy[1] > 0:
            result = number1 - number2
            operator_copy[1] -= 1
        elif operator_copy[2] > 0:
            result = number1 * number2
            operator_copy[2] -= 1

        numbers_copy.insert(0, result)
    return numbers_copy[0]

print(getMaxValue(numbers[:], operator[:]))
print(getMinValue(numbers[:], operator[:]))