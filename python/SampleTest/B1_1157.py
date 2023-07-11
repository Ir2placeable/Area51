# https://www.acmicpc.net/problem/1157
from collections import defaultdict
import sys

string = sys.stdin.readline().rstrip()
string = string.upper()

alphabets = defaultdict(int)
for char in string:
    alphabets[char] += 1

sorted_alphabets = list(sorted(alphabets.items(), key=lambda x: x[1], reverse=True))
result = sorted_alphabets[0][0]
if len(sorted_alphabets) > 1 and sorted_alphabets[0][1] == sorted_alphabets[1][1]:
    result = '?'

print(result)