# implementation by @kaba_y, https://korogba.github.io
from copy import deepcopy

from utils.file_operations import convert_file_to_tsp
from itertools import combinations, chain
from math import sqrt


def generate_subsets(cities, size) -> list:
    subsets = set(combinations(cities, size))
    list_of_subsets = []
    for each_set in subsets:
        if cities[0] not in each_set:
            continue
        bits = [0 if cities[x] not in each_set else 1 for x in range(len(cities))]
        list_of_subsets.append(bits)

    return list_of_subsets


def generate_base_sets(cities) -> list:
    set_of_cities = chain.from_iterable(combinations(cities, r) for r in range(len(cities) + 1))
    list_of_subsets = []
    for each_set in set_of_cities:
        if cities[0] not in each_set:
            continue
        bits = [0 if cities[x] not in each_set else 1 for x in range(len(cities))]
        list_of_subsets.append(bits)

    return list_of_subsets


def generate_key(s, j):
    destination = "{0:b}".format(j)
    s = "".join(map(str, s))
    key = s + destination
    return int(key, base=2)


def tsp(file_path) -> int:
    cities, size = convert_file_to_tsp(file_path)
    base_cases = generate_base_sets(cities)
    a = {generate_key(i, 0): (0 if 1 == sum(i) else float('inf')) for i in base_cases}
    for m in range(2, len(cities) + 1):
        gen_sets = generate_subsets(cities, m)
        for each_set in gen_sets:
            j_indices = [i for i, x in enumerate(each_set) if x == 1]
            for j in j_indices:
                if j == 0:
                    continue
                k_indices = [i for i, x in enumerate(each_set) if x == 1 and i != j]
                j_removed = deepcopy(each_set)
                j_removed[j] = 0
                k_distances = [a[generate_key(j_removed, k)] + get_dist(j, k, cities) for k in k_indices]
                a[generate_key(each_set, j)] = min(k_distances)

        print("Done with sub-problem size: ", m)

        # ToDO: Find feasible way to prune solutions: this seems to make no difference
        # remove_sets = generate_subsets(cities, (m - 1))
        # for i in range(1, len(cities) + 1):
        #     for del_set in remove_sets:
        #         del_key = generate_key(del_set, i)
        #         if del_key in a:
        #             del a[generate_key(del_set, i)]

    penultimate_set = [1 for _ in range(len(cities))]
    return min([a[generate_key(penultimate_set, j)] + get_dist(j, 0, cities) for j in range(1, len(cities))])


def get_dist(j, k, cities):
    return sqrt(pow(cities[j][0] - cities[k][0], 2) + pow(cities[j][1] - cities[k][1], 2))
