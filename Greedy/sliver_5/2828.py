# 2828 : 사과 담기 게임
# https://www.acmicpc.net/problem/2828

basket_index = 0
move_count = 0
screen_size, basket_size = map(lambda x: int(x), input().split(" "))
apples = int(input())

for i in range(0, apples):
    apple_index = int(input()) - 1

    if apple_index < basket_index:
        while apple_index < basket_index :
            move_count += 1
            basket_index -= 1
    elif basket_index + basket_size-1 < apple_index:
        while basket_index + basket_size-1 < apple_index:
            move_count += 1
            basket_index += 1
print(move_count)