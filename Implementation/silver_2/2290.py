# https://www.acmicpc.net/problem/2290

# s+2의 가로와 2s+3의 세로

import sys
n, string = sys.stdin.readline().split()
n = int(n)
maps = [[' ' for _ in range(len(string) * (n+2) + len(string))] for _ in range(2*n + 3)]


def seg1(base_x, base_y, size):
    for k in range(base_y + 1, base_y + 1 + size):
        maps[k][base_x + size + 1] = '|'


def seg2(base_x, base_y, size):
    for k in range(base_y + 2 + size, base_y + 2 + size + size):
        maps[k][base_x + size + 1] = '|'


def seg3(base_x, base_y, size):
    for k in range(base_x + 1, base_x + 1 + size):
        maps[base_y + size + size + 2][k] = '-'


def seg4(base_x, base_y, size):
    for k in range(base_y + 2 + size, base_y + 2 + size + size):
        maps[k][base_x] = '|'


def seg5(base_x, base_y, size):
    for k in range(base_y + 1, base_y + 1 + size):
        maps[k][base_x] = '|'


def seg6(base_x, base_y, size):
    for k in range(base_x + 1, base_x + 1 + size):
        maps[base_y][k] = '-'


def seg7(base_x, base_y, size):
    for k in range(base_x + 1, base_x + 1 + size):
        maps[base_y + 1 + size][k] = '-'


def one(base_x, base_y, size):
    seg1(base_x, base_y, size)
    seg2(base_x, base_y, size)


def two(base_x, base_y, size):
    seg6(base_x, base_y, size)
    seg1(base_x, base_y, size)
    seg3(base_x, base_y, size)
    seg4(base_x, base_y, size)
    seg7(base_x, base_y, size)


def three(base_x, base_y, size):
    seg6(base_x, base_y, size)
    seg1(base_x, base_y, size)
    seg2(base_x, base_y, size)
    seg3(base_x, base_y, size)
    seg7(base_x, base_y, size)


def four(base_x, base_y, size):
    seg1(base_x, base_y, size)
    seg2(base_x, base_y, size)
    seg5(base_x, base_y, size)
    seg7(base_x, base_y, size)


def five(base_x, base_y, size):
    seg2(base_x, base_y, size)
    seg3(base_x, base_y, size)
    seg5(base_x, base_y, size)
    seg6(base_x, base_y, size)
    seg7(base_x, base_y, size)


def six(base_x, base_y, size):
    seg2(base_x, base_y, size)
    seg3(base_x, base_y, size)
    seg4(base_x, base_y, size)
    seg5(base_x, base_y, size)
    seg6(base_x, base_y, size)
    seg7(base_x, base_y, size)


def seven(base_x, base_y, size):
    seg1(base_x, base_y, size)
    seg2(base_x, base_y, size)
    seg6(base_x, base_y, size)


def eight(base_x, base_y, size):
    seg1(base_x, base_y, size)
    seg2(base_x, base_y, size)
    seg3(base_x, base_y, size)
    seg4(base_x, base_y, size)
    seg5(base_x, base_y, size)
    seg6(base_x, base_y, size)
    seg7(base_x, base_y, size)


def nine(base_x, base_y, size):
    seg1(base_x, base_y, size)
    seg2(base_x, base_y, size)
    seg3(base_x, base_y, size)
    seg5(base_x, base_y, size)
    seg6(base_x, base_y, size)
    seg7(base_x, base_y, size)


def zero(base_x, base_y, size):
    seg1(base_x, base_y, size)
    seg2(base_x, base_y, size)
    seg3(base_x, base_y, size)
    seg4(base_x, base_y, size)
    seg5(base_x, base_y, size)
    seg6(base_x, base_y, size)

# 0, s+2,
for i in range(len(string)):
    char = string[i]
    x = i * (n+3)
    if char == '1':
        one(x, 0, n)
    elif char == '2':
        two(x, 0, n)
    elif char == '3':
        three(x, 0, n)
    elif char == '4':
        four(x, 0, n)
    elif char == '5':
        five(x, 0, n)
    elif char == '6':
        six(x, 0, n)
    elif char == '7':
        seven(x, 0, n)
    elif char == '8':
        eight(x, 0, n)
    elif char == '9':
        nine(x, 0, n)
    elif char == '0':
        zero(x, 0, n)
for temp in maps:
    print(''.join(temp))