# 3182 : 한동이는 공부가 하기 싫어!
# https://www.acmicpc.net/problem/3182

# 일단 한 명씩 시도해야함
import sys

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    people.append(int(sys.stdin.readline()))

max_val = 0
max_person = 0
# 한 사람으로 시작해서 몇번 순회하는지 체크한다.
for i in range(0, n):
    person = people[i] - 1
    called = [0] * n
    called[i] = 1
    count = 1

    while called[person] == 0:
        called[person] = 1
        count += 1
        person = people[person] - 1

    if count > max_val:
        max_val = count
        max_person = i

print(max_person + 1)