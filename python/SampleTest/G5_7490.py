# https://www.acmicpc.net/problem/7490

import sys
from copy import deepcopy


def GetValue(expression):
    new_expression = []
    temp = 0
    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '-':
            new_expression.append(temp)
            temp = 0
            new_expression.append(expression[i])
        elif expression[i] == ' ':
            temp = temp * 10
        else:
            temp += expression[i]
    new_expression.append(temp)

    result = new_expression[0]
    for i in range(1, len(new_expression)-1, 2):
        if new_expression[i] == '+':
            result += new_expression[i+1]
        else:
            result -= new_expression[i+1]

    return result


def makeFormat(expression):
    result = ''
    for temp in expression:
        result += str(temp)

    return result


def BFS(current_expression, number):
    if number == n+1:
        if GetValue(deepcopy(current_expression)) == 0:
            print(makeFormat(deepcopy(current_expression)))
        return

    for operator in operator_cases:
        next_expression = deepcopy(current_expression)
        next_expression.append(operator)
        next_expression.append(number)
        BFS(next_expression, number + 1)


test_cases = int(sys.stdin.readline())
operator_cases = [' ', '+', '-']
for i in range(test_cases):
    n = int(sys.stdin.readline())

    nums = [i for i in range(1, n+1)]
    BFS([1], 2)

    if i < test_cases - 1:
        print()