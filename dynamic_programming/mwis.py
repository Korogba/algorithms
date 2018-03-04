# implementation by @kaba_y, https://korogba.github.io
# mwis means maximum weight independent sent
from utils.file_operations import convert_file_to_list

find_indices = [1, 2, 3, 4, 17, 117, 517, 997]


def get_mwis(file_path) -> []:
    """todo: update docs"""
    vertex_list = convert_file_to_list(file_path)
    sub_solutions = []

    for i in range(len(vertex_list)):
        if i == 0:
            sub_solutions.append(vertex_list[i])
        elif i == 1:
            sub_solutions.append(max(sub_solutions[i - 1], vertex_list[i]))
        else:
            sub_solutions.append(max(sub_solutions[i - 1], sub_solutions[i - 2] + vertex_list[i]))

    vertex_set = []
    i = len(vertex_list) - 1
    bits = [0, 0, 0, 0, 0, 0, 0, 0]

    while i >= 1:
        # todo: hacky: look for cleaner solution
        if i == 1:
            # if sub_solutions[i - 1] >= sub_solutions[i - 2] + vertex_list[i]:
            #     vertex_set.append(vertex_list[i - 1])
            #     bits[1] = 1
            #     i -= 1
            # else:
            #     vertex_set.append(vertex_list[i])
            #     vertex_set.append(vertex_list[i - 2])
            #     bits[2] = 1
            #     bits[0] = 1
            #     i -= 1
            # continue
            if vertex_list[i - 1] >= vertex_list[i]:
                vertex_set.append(vertex_list[i - 1])
                if i in find_indices:
                    bits[find_indices.index(i)] = 1
                i -= 1
            else:
                vertex_set.append(vertex_list[i])
                if (i + 1) in find_indices:
                    bits[find_indices.index(i + 1)] = 1
                i -= 2
            continue
        if sub_solutions[i - 1] >= sub_solutions[i - 2] + vertex_list[i]:
            i -= 1
        else:
            vertex_set.append(vertex_list[i])
            if i == 2:
                bits[find_indices.index(i - 1)] = 1
            if (i + 1) in find_indices:
                bits[find_indices.index(i + 1)] = 1
            i -= 2

    return bits
