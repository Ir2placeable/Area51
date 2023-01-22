# https://www.acmicpc.net/problem/14658

# 단순 브루트포스 문제이다.
# 별똥별이 떨어질 가능성이 있는 좌표 -> maps
# maps 에 별똥별 좌표 기록
# maps 돌면서, 별똥별인 경우 -> 트랜펄린 크기 만큼 다시 돈다. -> 별통별의 개수 카운트 -> 최대인 것 찾기
# maps 크기 -> 500000 * 500000 -> 메모리 초과!

# 별똥별의 개수는 최대 100개로 정해져 있음
# 별똥별를 입력 받으면서 -> x좌표 리스트 / y좌표 리스트를 따로 저장해둠.
# 따로 저장한 x, y 리스트를 좌표의 기준으로 삼고 진행

import sys

width, height, trampoline, numOfStars = map(lambda x: int(x), sys.stdin.readline().split())
stars = []
x_list = []
y_list = []
for _ in range(numOfStars):
    x, y = map(lambda k: int(k), sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)
    stars.append([x, y])
# print(stars)

result = numOfStars
for x in x_list:
    for y in y_list:
        temp_result = numOfStars

        nx, ny = min(width, x+trampoline), min(height, y+trampoline)
        for sx, sy in stars:
            if x <= sx <= nx and y <= sy <= ny:
                temp_result -= 1
        
        result = min(result, temp_result)
print(result)