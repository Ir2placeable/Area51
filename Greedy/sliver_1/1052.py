# 1052 : 물병
# https://www.acmicpc.net/problem/1052

# 물병에 들어있는 물의 양은 중요하지 않다. 물이 있냐 없냐를 따지는 게 핵심이다.
# N개의 물병 중, K개의 물병에만 물을 채워야 한다.
# 같은 양의 물이 들어 있는 물병에서 1개만 뺄 수 있다.
# n의 값을 1, 2, 4, 8 ...로 만드는게 중요한 문제이다.

# 1차 시도 : # 2진수로 활용해야 한다.
# 결과 : 시간초과! -> N이 커질 때 문제가 생긴다.
# import sys
#
# n, k = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
#
#
# def count_bits(binary):
#     print(binary)
#     bits = 0
#     for bit in binary:
#         if bit == '1':
#             bits += 1
#
#     return bits
#
#
# bottles = 0
# while count_bits(bin(n)[2:]) != k:
#     n += 1
#     bottles += 1
#
# print(bottles)

# 2차 시도 : while 문이 돌아가는 조건을 줄이기 위해, 2진수의 비트수는 수의 길이 전까지 증가한다는 특징을 사용해보자
# ex) 1000 -> 1001 -> 1010 -> 1011.... 와 같이 항상 비트가 1개씩 증가한다.
# 따라서 현재 n의 비트 수가 k보다 많으면, 아예 비트수가 1이면서 큰 수로 초기화 하자.
# bottles의 계산은 결과값과 초기값의 차로 구한다.
import sys


def bit_count(number):
    bits = 0
    for bit in bin(number)[2:]:
        if bit == '1':
            bits += 1
    return bits


n1, k = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))

bottles = 0
bits = bit_count(n1)
n2 = n1
if bits < k:
    while bit_count(n2) != k:
        n2 += 1
elif k == 1:
    n2 = 2 ** len(bin(n1)[2:])
elif k == 2:
    n2 = 2 ** len(bin(n1)[2:])
elif bits > k:
    while bit_count(n2) != k:
        n2 += 1

print(n2 - n1)