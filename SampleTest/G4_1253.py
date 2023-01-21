# https://www.acmicpc.net/problem/1253

# '좋다' 수 리스트를 만들어 두고, 하나씩 '좋다' 수 인지 체크하는 방법이 떠오른다.
# 그러나, 입력 수의 크기가 10억 이다 -> O(n)으로 해야할 것 같다.

# 10
# 1 2 3 4 5 6 7 8 9 10

import sys

n = int(sys.stdin.readline())
numbers = list(map(lambda x: int(x), sys.stdin.readline().split()))
numbers.sort()
# print(numbers)

count = 0
for i in range(n-1, -1, -1):
    target_number = numbers[i]

    left = 0
    right = n-1
    while left < right:
        if left == i:
            left += 1
            continue
        elif right == i:
            right -= 1
            continue

        if numbers[left] + numbers[right] > target_number:
            right -= 1
        elif numbers[left] + numbers[right] < target_number:
            left += 1
        else:
            count += 1
            break

print(count)