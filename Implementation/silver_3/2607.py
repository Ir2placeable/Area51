# https://www.acmicpc.net/problem/2607

# 같은 구성이다 : 문자 개수가 같다 + 문자 종류가 같다
# 비슷한 단어이다 : 같은 구성이다 or 한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우

# 같은 구성인 것은 dictionary 로 판단이 가능하다.
# 비슷한 단어이다는 ....

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
base_word = sys.stdin.readline().rstrip()
words = []
for _ in range(n-1):
    words.append(sys.stdin.readline().rstrip())

result = 0
base_dict = defaultdict(int)
for char in base_word:
    base_dict[char] += 1

for target_word in words:
    temp_dict = base_dict.copy()

    for char in target_word:
        temp_dict[char] -= 1

    check1 = 0
    check2 = 0
    for _, value in temp_dict.items():
        if value == -1:
            check1 += 1
        elif value == 1:
            check2 += 1
        elif value == 0:
            continue
        else:
            check1 = 10
            break

    if check1 > 1 or check2 > 1:
        continue

    result += 1
print(result)