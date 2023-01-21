# https://www.acmicpc.net/problem/1253

# '좋다' 수 리스트를 만들어 두고, 하나씩 '좋다' 수 인지 체크하는 방법이 떠오른다.
# 그러나, 입력 수의 크기가 10억 이다 -> 시간 복잡도를 고려해야 한다.
# left, right 투 포인터를 이용해서 푸는 방법을 이용한다. -> 숫자가 정렬되어 있어야 한다.


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