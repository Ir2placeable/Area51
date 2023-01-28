# https://www.acmicpc.net/problem/21921

# X일 내에 방문자 수의 합 중 맥스를 구하는 문제이다. -> 이떄, X는 고정이다.
# 고정된 기간을 계속 움직이므로 -> 윈도우 슬라이딩 방식을 사용한다.
# 추가 조건 : 같은 맥스값인 경우 카운트 + 1
# 추가 조건2 : 맥스값이 0 인 경우 SAD

import sys
n, k = map(lambda x: int(x), sys.stdin.readline().split())
numbers = list(map(lambda x: int(x), sys.stdin.readline().split()))

max_value, max_count = 0, 1
window = sum(numbers[:k])
index = 0

while True:
    if window == max_value:
        max_count += 1
    elif window > max_value:
        max_value = window
        max_count = 1

    if index + k == n:
        break
    window -= numbers[index]
    window += numbers[index+k]
    index += 1


if max_value == 0:
    print('SAD')
else:
    print(max_value)
    print(max_count)
