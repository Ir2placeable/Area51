# https://www.acmicpc.net/problem/5073
import sys

while True:
    a, b, c = map(lambda x: int(x), sys.stdin.readline().split())
    if a == b == c == 0:
        break

    result = ''
    if a == b == c:
        result = 'Equilateral'
    elif a == 0 or b == 0 or c == 0:
        result = 'Invalid'
    elif max(a, b, c) >= a + b + c - max(a, b, c):
        result = 'Invalid'
    elif a == b or b == c or c == a:
        result = 'Isosceles'
    else:
        result = 'Scalene'

    print(result)