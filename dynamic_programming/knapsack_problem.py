# implementation by @kaba_y, https://korogba.github.io
from utils.file_operations import convert_file_to_knapsack


def knapsack(file_path) -> int:
    value_list, weight_list, capacity = convert_file_to_knapsack(file_path)
    solution = []

    # add rows:
    for x in range(len(value_list)):
        solution.append([])

    # initialize first column to zero
    for x in range(capacity + 1):
        solution[0].append(0)

    for i in range(1, len(value_list)):
        for x in range(capacity + 1):
            if x < weight_list[i]:
                solution[i].append(solution[i - 1][x])
            else:
                solution[i].append(max(solution[i - 1][x], (solution[i - 1][x - weight_list[i]] + value_list[i])))

    return solution[len(value_list) - 1][capacity]
