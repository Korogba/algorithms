# implementation by @kaba_y, https://korogba.github.io

from utils.file_operations import convert_file_to_knapsack


# runs at the same/better (not confirmed) then the recursive implementation
def knapsack(file_path) -> int:
    val_list, w_list, cap = convert_file_to_knapsack(file_path)
    solution = []

    # add two columns to only remember previous solution:
    for x in range(2):
        solution.append({})

    # initialize first column to zero
    for x in range(cap + 1):
        solution[0][x] = 0

    for i in range(1, len(val_list)):
        for x in range(cap + 1):
            if x < w_list[i]:
                solution[1][x] = solution[0][x]
            else:
                solution[1][x] = (max(solution[0][x], (solution[0][x - w_list[i]] + val_list[i])))

        solution[0] = solution[1]
        solution[1] = {}

    return solution[0][cap]
