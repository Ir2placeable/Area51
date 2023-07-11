def BFS(cur_cost, cur_position):
    for nex_position in range(n):
        if network[cur_position][nex_position] == 0:
            continue
        if visited[nex_position]:
            continue

        dist[start][nex_position] = cur_cost
        visited[nex_position] = True
        BFS(cur_cost + 1, nex_position)


test_case = int(input())
for case_number in range(1, test_case + 1):
    temp = list(map(lambda x: int(x), input().split()))
    n = temp[0]
    network = [temp[i:i + n] for i in range(1, len(temp) - 1, n)]

    dist = [[n + 1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    # start 에서 이어지는 모든 경로를 탐색한다.
    for start in range(n):
        visited = [False for _ in range(n)]
        visited[start] = True
        BFS(1, start)

    print(dist)