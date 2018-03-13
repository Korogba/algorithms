# implementation by @kaba_y, https://korogba.github.io
from utils.file_operations import convert_file_to_knapsack


def knapsack(file_path) -> int:
    value_list, weight_list, capacity = convert_file_to_knapsack(file_path)
    solution = []

    # add two columns to only remember previous solution:
    for x in range(2):
        solution.append({})

    # initialize first column to zero
    for x in range(capacity + 1):
        solution[0][x] = 0

    for i in range(1, len(value_list)):
        for x in range(capacity + 1):
            if x < weight_list[i]:
                solution[1][x] = solution[0][x]
            else:
                solution[1][x] = (max(solution[0][x], (solution[0][x - weight_list[i]] + value_list[i])))

        solution[0] = solution[1]
        solution[1] = {}

    return solution[0][capacity]
