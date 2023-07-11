# 1339 : 단어 수학
# https://www.acmicpc.net/problem/1339

# 제일 큰 수에 맞추어 자리수를 맞춘다.
# 실패! -> AB, BA 에서 항상 A=9 이지 않다. 만약 BA가 10개 들어온다면, 반례가 생긴다.
# import sys
#
# n = int(sys.stdin.readline())
# strings = []
# max_len = 0
# for _ in range(n):
#     temp = sys.stdin.readline().rstrip()
#     max_len = max(max_len, len(temp))
#     strings.append(temp)
#
# for i in range(n):
#     if len(strings[i]) < max_len:
#         strings[i] = (max_len - len(strings[i])) * '_' + strings[i]
#
# new_dict = {}
# index = 9
# for i in range(max_len):
#     # i : 자릿수
#     for string in strings:
#         if string[i] == '_':
#             continue
#         if string[i] not in new_dict:
#             new_dict[string[i]] = str(index)
#             index -= 1
#
# new_strings = []
# for string in strings:
#     temp = ''
#     for char in string:
#         if char == '_':
#             continue
#         temp += new_dict[char]
#     new_strings.append(temp)
#
# new_strings = list(map(lambda x: int(x), new_strings))
# print(new_strings)
# print(sum(new_strings))

# 2차 시도 : 각 자리 별로 가질 수 있는 합을 더해놓는다.
# 생각하기 어려운 아이디어이며, 일종의 스킬로 익혀야 한다.
import sys

n = int(sys.stdin.readline())
strings = []
for _ in range(n):
    strings.append(sys.stdin.readline().rstrip())

alphabets = {}
for string in strings:
    deci = 0
    for i in range(len(string)-1, -1, -1):
        if string[i] in alphabets:
            alphabets[string[i]] += (10 ** deci)
        else:
            alphabets[string[i]] = (10 ** deci)
        deci += 1

alphabets = sorted(alphabets.items(), key=lambda x: x[1], reverse=True)
index = 9
sum_val = 0
for alphabet in alphabets:
    sum_val += alphabet[1] * index
    index -= 1

print(sum_val)