# 그래프 간선에 가중치(환경 부담금)가 있다. -> 다익스트라
# 모든 정점을 통과해야 한다. -> 프림

MAX = 1000000 ** 2 + 1


def getCost(city1, city2):
    return E * ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


test_case = int(input())
for case_number in range(1, test_case + 1):
    n = int(input())
    x_locations = list(map(lambda x: int(x), input().split()))
    y_locations = list(map(lambda x: int(x), input().split()))
    E = float(input())

    cities = []
    for i in range(n):
        cities.append([x_locations[i], y_locations[i]])
    visited_cities = [cities.pop()]

    total_cost = 0
    while cities:
        min_cost = MAX
        next_city = []

        for visited_city in visited_cities:
            for left_city in cities:
                cost = getCost(visited_city, left_city)
                if cost < min_cost:
                    next_city = left_city
                    min_cost = cost

        cities.remove(next_city)
        visited_cities.append(next_city)
        total_cost += min_cost

    result = round(total_cost)
    print("#%d %d" % (case_number, result))