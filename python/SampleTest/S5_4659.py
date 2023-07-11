# https://www.acmicpc.net/problem/4659

# 모음 1개 이상 포함
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

import sys

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    string = sys.stdin.readline().rstrip()
    if string == 'end':
        break

    result = '<' + string + '> '

    # condition1:
    condition1 = False
    for char in string:
        if char in vowel:
            condition1 = True
    if not condition1:
        result += 'is not acceptable.'
        print(result)
        continue

    # condition2
    condition2 = True
    for i in range(len(string)-2):
        a, b = 0, 0
        for char in string[i:i+3]:
            if char in vowel:
                a += 1
            else:
                b += 1
        if a == 3 or b == 3:
            condition2 = False
            break
    if not condition2:
        result += 'is not acceptable.'
        print(result)
        continue

    # condition3
    condition3 = True
    for i in range(len(string)-1):
        if string[i:i+2] == 'ee' or string[i:i+2] == 'oo':
            continue
        if string[i] == string[i+1]:
            condition3 = False
            break
    if not condition3:
        result += 'is not acceptable.'
        print(result)
        continue

    result += 'is acceptable.'
    print(result)