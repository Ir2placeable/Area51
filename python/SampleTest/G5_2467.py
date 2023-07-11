# https://www.acmicpc.net/problem/2467

# 두 용액을 무조건 합쳐야 한다. -> 혼합용액
# 혼합용액의 특성값이 0에 가까워야 한다.
# 그렇다면, 어떤 용액끼리 섞어야 할까 -> 핵심
# 용액이 정렬되서 주어진다. 왼쪽에서 하나 오른쪽에서 하나 선택해야 한다. -> 투 포인터 이용

import sys
n = int(sys.stdin.readline())
numbers = list(map(lambda x: int(x), sys.stdin.readline().split()))

result = [numbers[0], numbers[-1]]
mixed = sys.maxsize
left, right = 0, n-1
while left < right:
    temp_mixed = numbers[left] + numbers[right]
    if abs(temp_mixed) < mixed:
        mixed = abs(temp_mixed)
        result = [numbers[left], numbers[right]]

    if temp_mixed < 0:
        left += 1
    elif temp_mixed > 0:
        right -= 1
    else:
        break
print(*result)