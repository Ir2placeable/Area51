# 12904 : A와 B
# https://www.acmicpc.net/problem/12904

# 문자열의 뒤에 A를 추가한다. -> A 제거
# 문자열을 뒤집고 뒤에 B를 추가한다. -> B 제거 + 뒤집기

import sys
string1 = sys.stdin.readline().rstrip()
string2 = sys.stdin.readline().rstrip()


def removeLastChar(string):
    return string[:-1]


def upsideDownString(string):
    result = ''
    for i in range(len(string)-1, -1, -1):
        result += string[i]
    return result


while len(string2) != len(string1):
    if string2[-1] == 'A':
        string2 = removeLastChar(string2)
    elif string2[-1] == 'B':
        string2 = removeLastChar(string2)
        string2 = upsideDownString(string2)
    else:
        break

if string1 == string2:
    print(1)
else:
    print(0)
