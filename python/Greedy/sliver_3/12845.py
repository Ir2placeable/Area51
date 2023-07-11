# 12845 : 모두의 마블
# https://www.acmicpc.net/problem/12845
import sys

n = int(sys.stdin.readline())
card_list = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
card_list.sort()

gold = 0
while len(card_list) > 1:
    card1 = card_list.pop()
    card2 = card_list.pop()
    new_card = max(card1, card2)
    card_list.append(new_card)
    gold += card1 + card2

print(gold)