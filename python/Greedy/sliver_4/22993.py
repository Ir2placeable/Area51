# 22993 : 서든어택 3
# https://www.acmicpc.net/problem/22993

input()
people = list(map(lambda x: int(x), input().split(" ")))
heroine = people[0]
people = people[1:]
people.sort()

flag = True
for person in people:
    if heroine <= person:
        flag = False
        break
    heroine += person

if flag:
    print('Yes')
else:
    print('No')
