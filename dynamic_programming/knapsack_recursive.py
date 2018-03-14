# implementation by @kaba_y, https://korogba.github.io
import sys

from utils.file_operations import convert_file_to_knapsack

# throws a maximum resursion depth exceeded if this the limit is not raised
sys.setrecursionlimit(3000)
value_list, weight_list, capacity = convert_file_to_knapsack('../input_random_44_2000000_2000.txt')
found_solutions = {}
sorted_weights = sorted(weight_list)


def knapsack_recursive(i, cap) -> int:
    if i == 0 or cap == 0:
        return 0

    if (i, cap) in found_solutions:
        return found_solutions[(i, cap)]

    if weight_list[i] > cap:
        found_solutions[(i, cap)] = knapsack_recursive(i - 1, cap)
    else:
        found_solutions[(i, cap)] = max(knapsack_recursive(i - 1, cap),
                                        knapsack_recursive(i - 1, cap - weight_list[i]) + value_list[i])

    return found_solutions[(i, cap)]


print(knapsack_recursive(len(value_list) - 1, capacity))
