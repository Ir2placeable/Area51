# https://www.acmicpc.net/problem/17413

# < > 사이의 문자는 뒤집지 않는다.
# 단어 구분은 공백, <, > 세 가지 방법으로 한다.
import sys

string = sys.stdin.readline().rstrip()

result = ''
word = ''
bracket = False
for char in string:
    if char == '<':
        result += word[::-1]
        word = ''

        bracket = True
        word += char

    elif char == '>':
        word += char
        bracket = False

        result += word
        word = ''

    elif char == ' ':
        if bracket:
            word += char
        else:
            result += word[::-1] + ' '
            word = ''
    else:
        word += char

if string[-1] != '>':
    result += word[::-1]
print(result)