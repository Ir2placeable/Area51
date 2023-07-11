import sys

while True:
    a, b, c = map(lambda x: int(x), sys.stdin.readline().split())
    if a == b == c == 0:
        break

    a, b, c = sorted([a, b, c])
    if a + b <= c:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')