# 21313 : 문어
# https://www.acmicpc.net/problem/21313

# 서로 같은 번호의 손을 잡아야 한다.
# 한 문어와 둘 이상의 손을 잡을 수 없다.
# 한 손으로 여러 문어의 손을 잡을 수 없다.

# 사전 순으로 출력해야함 -> 1부터 시작해보자

num_of_octos = int(input())

hands = ''
for i in range(0, num_of_octos // 2):
    hands += '1 2 '
if num_of_octos % 2 == 1:
    hands += '3'
else:
    hands = hands[:-1]

print(hands)