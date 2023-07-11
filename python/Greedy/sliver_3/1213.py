# 1213 : 펠린드롬 만들기
# https://www.acmicpc.net/problem/1213

string = input()
alphabet = {}

for char in string:
    if char in alphabet:
        alphabet[char] += 1
    else:
        alphabet[char] = 1
alphabet = sorted(alphabet.items(), key=lambda x: x[0])

result = ''
mid = ''
flag = True
while alphabet:
    char = alphabet.pop()
    if char[1] % 2 == 1 and mid == '':
        mid = char[0]
    elif char[1] % 2 == 1 and mid != '':
        flag = False
        break

    for i in range(0, char[1]//2):
        result = char[0] + result + char[0]

if flag:
    result = result[0:len(result)//2] + mid + result[len(result)//2:]
else:
    result = 'I\'m Sorry Hansoo'
print(result)