# 15903 : 카드 합체 놀이
# https://www.acmicpc.net/problem/15903

# 카드를 합체할 때 마다 정렬을 해주면 된다. -> 우선순위 큐
import sys

n, k = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
cards = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))

while k > 0:
    cards.sort()

    temp = cards[0] + cards[1]
    cards[0] = temp
    cards[1] = temp
    k -= 1

print(sum(cards))