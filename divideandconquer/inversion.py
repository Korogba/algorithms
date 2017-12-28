# implementation by @kaba_y, https://korogba.github.io
SORTED_LIST = "sorted_list"
COUNT = "count"


def merge_split_count(left_sorted_count, right_sorted_count) -> dict:
    sorted_list = []
    i, j, split_count = 0, 0, 0

    while i < len(left_sorted_count) and j < len(right_sorted_count):
        if left_sorted_count[i] <= right_sorted_count[j]:
            sorted_list.append(left_sorted_count[i])
            i += 1
        else:
            sorted_list.append(right_sorted_count[j])
            j += 1
            split_count += len(left_sorted_count[i:])

    if i < len(left_sorted_count):
        sorted_list.extend(left_sorted_count[i:])
    if j < len(right_sorted_count):
        sorted_list.extend(right_sorted_count[j:])

    return {SORTED_LIST: sorted_list, COUNT: split_count}


def merge_sort_and_split_inversions(number_list) -> dict:
    """
    Count the number of inversions in the list. Uses recursive merge sort to count the number of inversions
    :param number_list: list of numbers to operate on
    :return: the number of inversions
    """
    n = len(number_list)
    if n == 1:
        return {SORTED_LIST: number_list, COUNT: 0}
    else:
        left_sorted_count = merge_sort_and_split_inversions(number_list[:n // 2])
        right_sorted_count = merge_sort_and_split_inversions(number_list[n // 2:])
        split_sorted_count = merge_split_count(left_sorted_count[SORTED_LIST], right_sorted_count[SORTED_LIST])
        inversion_count = split_sorted_count[COUNT] + left_sorted_count[COUNT] + right_sorted_count[COUNT]
        return {SORTED_LIST: split_sorted_count[SORTED_LIST], COUNT: inversion_count}
