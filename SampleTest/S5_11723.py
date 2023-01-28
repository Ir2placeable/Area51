# https://www.acmicpc.net/problem/11723

# 간단한 set 다루기 문제로 보인다.
# 메모리 제한이 있기 때문에, list 를 사용할 수 없다.
import sys

numbers = set([])
n = int(sys.stdin.readline())
for _ in range(n):
    temp = list(sys.stdin.readline().split())
    if len(temp) == 1:
        if temp[0] == 'all':
            numbers = set([str(i) for i in range(1, 21)])
        elif temp[0] == 'empty':
            numbers.clear()
    else:
        if temp[0] == 'add':
            numbers.add(temp[1])
        elif temp[0] == 'remove':
            numbers.discard(temp[1])
        elif temp[0] == 'check':
            if temp[1] in numbers:
                print(1)
            elif temp[1] not in numbers:
                print(0)
        elif temp[0] == 'toggle':
            numbers.discard(temp[1])
            if temp[1] in numbers:
                numbers.discard(temp[1])
            elif temp[1] not in numbers:
                numbers.add(temp[1])
