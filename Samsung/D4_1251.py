# 간선이 정해지지 않은 다익스트라 -> 프림 알고리즘

maxsize = 1000000**2 + 1


def GetCost(_from, _to):
    global e
    return e * ((_from[0] - _to[0]) ** 2 + (_from[1] - _to[1]) ** 2)


t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    locationX = list(map(lambda x: int(x), input().split()))
    locationY = list(map(lambda x: int(x), input().split()))
    e = float(input())

    cities = [[locationX[i], locationY[i]] for i in range(n)]
    result = 0
    visited = [cities.pop()]

    while cities:
        min_distance = maxsize
        min_city = []
        for visited_city in visited:
            for next_city in cities:
                distance = GetCost(visited_city, next_city)
                if min_distance > distance:
                    min_distance = distance
                    min_city = next_city

        result += min_distance
        visited.append(min_city)
        cities.remove(min_city)

    result = round(result)
    print("#%d %d" % (test_case, result))