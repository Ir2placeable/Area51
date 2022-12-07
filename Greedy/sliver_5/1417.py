# 1417 : 국회의원 선거
# https://www.acmicpc.net/problem/1417

# 기호 1번이 제일 커야 함
# max인 사람의 표를 -1 / 기호 1번의 표를 + 1

def isTop(list):
    for i in range(1, len(list)):
        if list[i] >= list[0]:
            return False
    return True


def top_index(list):
    x = 0
    for i in range(1, len(list)):
        if list[i] >= list[x]:
            x = i
    return x


N = int(input())
people = []

for i in range(0, N):
    people.append(int(input()))

taken_vote = 0

while not isTop(people):
    index = top_index(people)
    people[0] += 1
    people[index] -= 1
    taken_vote += 1

print(taken_vote)