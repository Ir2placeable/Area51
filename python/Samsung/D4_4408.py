# 그리디 문제
# 강의실 문제와 유사하다고 생각된다.

# 28분 컷

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    people = []
    for _ in range(n):
        a, b = map(lambda x: int(x), input().split())
        if a > b:
            a, b = b, a
        people.append([a, b])
    people.sort(key=lambda x: x[0])

    result = 0
    while people:
        result += 1
        target = people[0][1]
        remove_list = [0]

        for i in range(1, len(people)):
            # 홀수인경우
            if target % 2 == 1:
                if people[i][0] > target + 1:
                    target = people[i][1]
                    remove_list.append(i)
            else:
                if people[i][0] > target:
                    target = people[i][1]
                    remove_list.append(i)
        while remove_list:
            people.pop(remove_list.pop())

    print("#%d %d" % (test_case, result))