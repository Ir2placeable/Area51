# 15321 : 이름 궁합
# https://www.acmicpc.net/problem/15312
import sys
from collections import deque

alphabets = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
string1 = sys.stdin.readline().rstrip()
string2 = sys.stdin.readline().rstrip()

numbers = deque([])
for i in range(len(string1)):
    numbers.append(alphabets[ord(string1[i]) - 65])
    numbers.append(alphabets[ord(string2[i]) - 65])

while len(numbers) > 2:
    temp = []
    for i in range(0, len(numbers) - 1):
        temp.append((numbers[i] + numbers[i+1]) % 10)
    numbers = temp
    # print(temp)
print(str(numbers[0]) + str(numbers[1]))