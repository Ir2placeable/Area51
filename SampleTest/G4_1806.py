# https://www.acmicpc.net/problem/1806

# 스위핑 부분합 + 브루트포스 문제인 것 같음.
# 시작 인덱스를 브루트포스로 해보자
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