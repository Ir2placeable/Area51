# https://www.acmicpc.net/problem/11723

# 간단한 set 다루기 문제로 보인다.
import sys

numbers = set()
n = int(sys.stdin.readline())
for _ in range(n):
    temp = list(sys.stdin.readline().split())
    if temp[0] == 'all':
        numbers = set([i for i in range(1, 21)])
    elif temp[0] == 'empty':
        numbers = set()
    elif temp[0] == 'add':
        numbers.add(temp[1])
    elif temp[0] == 'remove':
        numbers.discard(temp[1])
    elif temp[0] == 'check':
        if temp[1] in numbers:
            print(1)
        else:
            print(0)
    elif temp[0] == 'toggle':
        if temp[1] in numbers:
            numbers.discard(temp[1])
        else:
            numbers.add(temp[1])