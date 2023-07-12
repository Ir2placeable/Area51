import sys
from collections import defaultdict

string = list(sys.stdin.readline().rstrip())

alphabets = defaultdict(int)
for char in string:
    alphabets[char] += 1

odd, odd_count = '', 0
for single_alphabet in alphabets:
    if alphabets[single_alphabet] % 2 == 1:
        odd = single_alphabet
        odd_count += 1
        alphabets[single_alphabet] -= 1

result = ''
if odd_count > 1: # 펠린드롬 불가
    result = "I'm Sorry Hansoo"
else:
    alphabets = sorted(alphabets.items(), key=lambda x: x[0])
    for single_alphabet, count in alphabets:
        result += single_alphabet * (count//2)

    result = result + odd + result[::-1]
print(result)
