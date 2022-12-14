# 13417 : 카드 문자열
# https://www.acmicpc.net/problem/13417
import sys

test_case = int(sys.stdin.readline())

for i in range(0, test_case):
    num_cards = int(sys.stdin.readline())
    card_list = list(sys.stdin.readline().rstrip().split(" "))

    if num_cards == 1:
        print(card_list[0])
    elif num_cards > 1:
        cur = card_list.pop(0)
        result = ''

        while len(card_list) > 1:
            nex = card_list.pop(0)

            if nex < cur:
                result += nex
                cur = nex

            else:
                card_list.append(nex)
        print(result)
