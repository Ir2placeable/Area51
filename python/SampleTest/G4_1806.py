# https://www.acmicpc.net/problem/1806

# left, right 투 포인터로 풀면 그만이야~
import sys

n, target = map(lambda x: int(x), sys.stdin.readline().split())
numbers = list(map(lambda x: int(x), sys.stdin.readline().split()))
# print(numbers)

left = 0
right = 0
acc = numbers[0]

result = sys.maxsize
while right < n :
    if acc < target:
        right += 1
        if right == n:
            break
        acc += numbers[right]
    else:
        result = min(result, right-left + 1)
        # print(left, right, acc)
        acc -= numbers[left]
        left += 1

if result == sys.maxsize:
    result = 0

print(result)