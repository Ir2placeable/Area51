def makeSchedule(current_index, current_path, current_score, current_time, isLastDay):
    global airport, single_score, single_path

    if isLastDay:
        if current_time + getCost[current_index][airport] <= 540 and single_score < current_score:
            single_score = current_score
            single_path = current_path + [airport]
    else:
        for hotel_index in hotels:
            if current_time + getCost[current_index][hotel_index] <= 540 and single_score < current_score:
                single_score = current_score
                single_path = current_path + [hotel_index]

    for index, time, score in points:
        if visited[index]:
            continue
        visited[index] = True
        makeSchedule(index, current_path + [index], current_score + score,
                     current_time + getCost[current_index][index] + time, isLastDay)
        visited[index] = False


test_case = int(input())
for case_number in range(1, test_case + 1):
    n, m = map(lambda x: int(x), input().split())
    getCost = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n - 1):
        temp = list(map(lambda x: int(x), input().split()))
        for j in range(len(temp)):
            getCost[i][j + i + 1] = temp[j]
            getCost[j + i + 1][i] = temp[j]

    airport, hotels, points = 0, [], []
    for i in range(n):
        temp = input().split()
        if temp[0] == 'A':
            airport = i
        elif temp[0] == 'H':
            hotels.append(i)
        elif temp[0] == 'P':
            points.append([i, int(temp[1]), int(temp[2])])

    ###
    current_index = airport
    total_path = []
    total_score = 0
    visited = [False for _ in range(n)]

    for day in range(1, m + 1):
        single_score = 0
        single_path = []
        if day == m:
            makeSchedule(current_index, [], 0, 0, True)
        else:
            makeSchedule(current_index, [], 0, 0, False)

        if not single_path:
            break
        total_path += single_path
        current_index = single_path.pop()
        for point_index in single_path:
            visited[point_index] = True
        total_score += single_score

    if not total_path:
        print("#%d %d" % (case_number, total_score))
    else:
        total_path = list(map(lambda x: str(x + 1), total_path))
        result = ' '.join(total_path)
        print("#%d %d" % (case_number, total_score), result)