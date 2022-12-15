# 13417 : 카드 문자열
# https://www.acmicpc.net/problem/13417
import sys

test_case = int(sys.stdin.readline())

for i in range(0, test_case):
    num_cards = int(sys.stdin.readline())
    card_list = list(sys.stdin.readline().rstrip().split(" "))

    if num_cards == 1:
        print(card_list[0])
        continue

    result = card_list.pop(0)
    while len(card_list) > 0:
        card = card_list.pop(0)

        if card <= result[0]:
            result = card + result
        else:
            result = result + card

    print(result)