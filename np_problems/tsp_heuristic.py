# implementation by @kaba_y, https://korogba.github.io
from math import sqrt
from utils.file_operations import convert_file_to_tsp_heuristics


def get_dist(j, k, cities):
    return sqrt(pow(cities[j][0] - cities[k][0], 2) + pow(cities[j][1] - cities[k][1], 2))


# Not used because used in get_all_distances(cities, size)
def get_key(i, j, n):
    key_bits = [1 if x == i or x == j else 0 for x in range(n)]
    key = int("".join(str(bit) for bit in key_bits), 2)
    return key


# Not used because boy! did it slow down the algorithm! Estimated time for completion was 24 hours ? ¯\_(ツ)_/¯
def get_all_distances(cities, size) -> dict:
    distances = {}
    for i in range(size):
        for j in range((i + 1), size):
            key = get_key(i, j, size)
            distances[key] = get_dist(i, j, cities)

    return distances


def get_closest_neighbor(i, visited_indices, cities) -> tuple:
    min_distance = float('inf')
    closest_neighbor_idx = -1
    for j in range(len(cities)):
        if j not in visited_indices:
            distance = get_dist(i, j, cities)
            if distance < min_distance:
                min_distance = distance
                closest_neighbor_idx = j

    return closest_neighbor_idx, min_distance


def tsp_with_nearest_distance_heuristics(file_path) -> int:
    cities, size = convert_file_to_tsp_heuristics(file_path)
    tsp_cost = 0
    i = 0
    visited_indices = set()

    for _ in range(len(cities)):
        visited_indices.add(i)
        if len(visited_indices) == len(cities):
            break
        i, min_distance = get_closest_neighbor(i, visited_indices, cities)
        tsp_cost += min_distance

    tsp_cost += get_dist(i, 0, cities)

    return tsp_cost
