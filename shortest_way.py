from itertools import permutations

coordinates = {'A': (0, 2), 'B': (2, 5), 'C': (5, 2), 'D': (6, 6), 'E': (8, 3)}


def find_all_distance(c):
    distances = {}
    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            x = list(c.values())[i]
            y = list(c.values())[j]
            length = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
            distances[f'{chr(65 + i)}{chr(65 + j)}'] = length
            distances[f'{chr(65 + j)}{chr(65 + i)}'] = length
    return distances


def find_the_shortest_way(d):
    shortest_route = {'': list(d.values())}
    for i in permutations(list(coordinates.keys()), len(coordinates)):
        if i[0] == 'A':
            combs = ''.join(i) + 'A'
            total = []
            for j in range(len(combs) - 1):
                amount = d.get(combs[j] + combs[j + 1])
                total.append(amount)
            if sum(total) < sum(list(shortest_route.values())[0]):
                shortest_route = {combs: total}
    return shortest_route


def result_output(c, s):
    print(f'{c.get(list(s.keys())[0][0])} ', end='')
    for i in range(1, len(c) + 1):
        print(f'-> {c.get(list(s.keys())[0][i])}{[sum(list(s.values())[0][:i])]} ', end='')
    print(f'= {sum(list(s.values())[0])}')


a = find_all_distance(coordinates)
b = find_the_shortest_way(a)

result_output(coordinates, b)
