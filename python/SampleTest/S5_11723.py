# https://www.acmicpc.net/problem/11723

# 간단한 set 다루기 문제로 보인다.
# 메모리 제한이 있기 때문에, list 를 사용할 수 없다.
import sys

numbers = set([])
n = int(sys.stdin.readline())
for _ in range(n):
    temp = sys.stdin.readline().strip().split()
    if len(temp) == 1:
        if temp[0] == 'all':
            numbers = set([i for i in range(1, 21)])
        else:
            numbers = set()
    else:
        operator, num = temp[0], int(temp[1])
        
        if operator == 'add':
            numbers.add(num)
        elif operator == 'remove':
            numbers.discard(num)
        elif operator == 'check':
            if num in numbers:
                print(1)
            else:
                print(0)
        elif operator == 'toggle':
            if num in numbers:
                numbers.discard(num)
            else:
                numbers.add(num)
