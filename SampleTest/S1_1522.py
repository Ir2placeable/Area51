# https://www.acmicpc.net/problem/1522

# b가 연속으로 이어져야 한다.
# 이때, 연속으로 이어진 문자열은 b의 개수와 동일하다. -> 슬라이딩 윈도우이다.
# 윈도우를 b의 개수로 고정하고, 문자열을 슬라이딩 하면서 b 개수의 최대 값을 구한다.
# a, b를 서로 교체하는 행위는 논리적으로 생각할 필요가 없다. 어차피 교체되는 것이니
# 교체 횟수는 "b의 총 개수 - b의 최대 개수" 이다.

import sys

string = list(sys.stdin.readline().rstrip())
window_size = string.count('b')

# a, b
b = 0
for i in range(window_size):
    if string[i] == 'b':
        b += 1

max_b = b
for i in range(0, len(string)):
    if string[i] == 'b':
        b -= 1
    if string[(i+window_size)%len(string)] == 'b':
        b += 1
    max_b = max(max_b, b)

print(window_size - max_b)