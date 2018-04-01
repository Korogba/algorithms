# implementation by @kaba_y, https://korogba.github.io
from math import sqrt
from copy import deepcopy
from utils.file_operations import convert_file_to_tsp_heuristics


def get_dist(j, k, cities):
    return sqrt(pow(cities[j][0] - cities[k][0], 2) + pow(cities[j][1] - cities[k][1], 2))


def get_key(i, j, n):
    key_bits = [1 if x == i or x == j else 0 for x in range(n)]
    key = int("".join(str(bit) for bit in key_bits), 2)
    return key


def get_all_distances(cities, size) -> dict:
    distances = {}
    for i in range(size):
        for j in range((i + 1), size):
            key = get_key(i, j, size)
            distances[key] = get_dist(i, j, cities)

    return distances


def tsp_with_nearest_distance_heuristics(file_path) -> int:
    cities, size = convert_file_to_tsp_heuristics(file_path)
    # distances = get_all_distances(cities, size)
    # print("Done with distances!")
    working_copy = deepcopy(cities)
    tsp_cost = 0
    i = 0
    while working_copy:
        city = working_copy.pop(i)
        city_idx = cities.index(city)
        min_distance = float('inf')
        if working_copy:
            for j in range(len(working_copy)):
                neighbor_idx = cities.index(working_copy[j])
                # distance = distances[get_key(city_idx, neighbor_idx, size)]
                distance = get_dist(city_idx, neighbor_idx, cities)
                if distance < min_distance:
                    min_distance = distance
                    i = j
        else:
            # min_distance = distances[get_key(city_idx, 0, size)]
            min_distance = get_dist(city_idx, 0, cities)

        tsp_cost += min_distance
        print("Current city size: ", len(working_copy))

    return tsp_cost
