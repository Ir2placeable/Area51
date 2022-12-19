# 1541 : 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
import sys

string = sys.stdin.readline().rstrip()

items = []
item = ''
for char in string:
    if char == '+':
        items.append(int(item))
        items.append('+')
        item = ''
    elif char == '-':
        items.append(int(item))
        items.append('-')
        item = ''
    else:
        item += char
items.append(int(item))

minus = False
result = 0
for item in items:
    if item == '-':
        minus = True
        continue

    if type(item) == int:
        if minus:
            result -= item
        else:
            result += item

print(result)