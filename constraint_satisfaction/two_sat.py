# implementation by @kaba_y, https://korogba.github.io
from bisect import bisect_left
from math import log
from random import random

from utils.file_operations import convert_file_to_two_sat


def assign_random_values(variable_length) -> []:
    return [random() < 0.5 for _ in range(variable_length)]


def satisfies_constraints(random_assignments, variables, clauses) -> tuple:
    for i in clauses:
        x, y = i
        x_idx = variables.index(max(x, (-1 * x)))
        y_idx = variables.index(max(y, (-1 * y)))
        bool_x = random_assignments[x_idx] if x > 0 else not random_assignments[x_idx]
        bool_y = random_assignments[y_idx] if y > 0 else not random_assignments[y_idx]

        if not (bool_x or bool_y):
            return False, x_idx, y_idx

    return True, None, None


def flip_arbitrary_clause(random_assignments, x_idx, y_idx) -> None:
    if random() < 0.5:
        random_assignments[x_idx] = not random_assignments[x_idx]
    else:
        random_assignments[y_idx] = not random_assignments[y_idx]


def prune_clauses(clauses, variables, positive_set, negative_set):
    count = 0
    while len(positive_set ^ negative_set) > 0 and count < 150:
        count += 1
        symmetric_dif = positive_set ^ negative_set
        positive_set.clear()
        negative_set.clear()
        del_ids = []
        for clause in clauses:
            if max(clause[0], -1 * clause[0]) in symmetric_dif \
                    or max(clause[1], -1 * clause[1]) in symmetric_dif:
                del_ids.append(clause)
            else:
                if clause[0] < 0:
                    negative_set.add(-1 * clause[0])
                else:
                    positive_set.add(clause[0])

                if clause[1] < 0:
                    negative_set.add(-1 * clause[1])
                else:
                    positive_set.add(clause[1])

        for clause in del_ids:
            del clauses[clause]

    variables.clear()
    for clause in clauses:
        left_var = clause[0]
        left_var = max(left_var, (-1 * left_var))
        left_idx = bisect_left(variables, left_var)
        if not (left_idx != len(variables) and variables[left_idx] == left_var):
            variables.insert(left_idx, left_var)

        right_var = clause[1]
        right_var = max(right_var, (-1 * right_var))
        right_idx = bisect_left(variables, right_var)
        if not (right_idx != len(variables) and variables[right_idx] == right_var):
            variables.insert(right_idx, right_var)


def papadimitriou(file_path) -> int:
    clauses, variables, positive_set, negative_set = convert_file_to_two_sat(file_path)
    prune_clauses(clauses, variables, positive_set, negative_set)
    random_trials = log(len(variables))
    repeat = 2 * pow(len(variables), 2)

    for _ in range(int(random_trials)):
        random_assignments = assign_random_values(len(variables))
        for __ in range(repeat):
            satisfies, x_idx, y_idx = satisfies_constraints(random_assignments, variables, clauses)
            if satisfies:
                return 1
            flip_arbitrary_clause(random_assignments, x_idx, y_idx)

    return 0
