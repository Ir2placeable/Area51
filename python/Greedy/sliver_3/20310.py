# 20310 : 타노스
# https://www.acmicpc.net/problem/20310
import sys

string = sys.stdin.readline().rstrip()

string_list = []
zero, one = 0, 0
for char in string:
    if char == '0':
        zero += 1
    else:
        one += 1
    string_list.append(char)

zero //= 2
one //= 2

result = ''
for i in range(0, len(string_list)):
    if one == 0:
        break

    if string_list[i] == '1':
        string_list[i] = 'x'
        one -= 1
for i in range(len(string_list)-1, -1, -1):
    if zero == 0:
        break

    if string_list[i] == '0':
        string_list[i] = 'x'
        zero -= 1

for item in string_list:
    if item == 'x':
        continue

    result += item

print(result)