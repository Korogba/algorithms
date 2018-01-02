# implementation by @kaba_y, https://korogba.github.io
from statistics import median


# Because I struggled to get a global variable in imperative python, besides global variables are bad, right?
class TestClass:
    global_count = 0


def partition(input_list, left, right) -> int:
    pivot = input_list[left]
    i = left + 1
    count = 0
    for j in range((left + 1), right + 1):
        # Remove:
        # TestClass.global_count += 1
        count += 1
        if input_list[j] < pivot:
            input_list[j], input_list[i] = input_list[i], input_list[j]
            i += 1
    input_list[left], input_list[i - 1] = input_list[i - 1], input_list[left]

    # ToDo: This if clause seems unnecessary investigate and introduced a subtle bug, why?!!!
    # if i >= right:
    #     return right
    return input_list.index(pivot)


def pre_process_median_pivot(input_list, low, high):
    first = input_list[low]
    last = input_list[high]
    # The middle index is an offset from low, and low changes depending on the partition so add low
    middle = input_list[((high - low) // 2) + low]

    pivot_index = input_list.index(median([first, last, middle]))
    input_list[low], input_list[pivot_index] = input_list[pivot_index], input_list[low]


def pre_process_last_element_pivot(input_list, low, high):
    input_list[low], input_list[high] = input_list[high], input_list[low]


def quicksort_with_first_element_pivot(input_list, low, high) -> int:
    if len(input_list) == 1:
        return 0
    if low < high:
        comparison_count = 0
        # no need to pre-process since pivot always occupies the first position
        partition_index = partition(input_list, low, high)
        comparison_count += high - low
        if partition_index > low:
            comparison_count += quicksort_with_first_element_pivot(input_list, low, partition_index - 1)
        if partition_index < high:
            comparison_count += quicksort_with_first_element_pivot(input_list, partition_index + 1, high)

        return comparison_count
    else:
        return 0


def quicksort_with_last_element_pivot(input_list, low, high) -> int:
    if len(input_list) == 1:
        return 0
    if low < high:
        comparison_count = 0
        # pre-process input list and make the last element the pivot
        pre_process_last_element_pivot(input_list, low, high)
        partition_index = partition(input_list, low, high)
        comparison_count += high - low
        if partition_index > low:
            comparison_count += quicksort_with_last_element_pivot(input_list, low, partition_index - 1)
        if partition_index < high:
            comparison_count += quicksort_with_last_element_pivot(input_list, partition_index + 1, high)

        return comparison_count
    else:
        return 0


def quicksort_with_median_pivot(input_list, low, high) -> int:
    if len(input_list) == 1:
        return 0
    if low < high:
        comparison_count = 0
        # pre-process input list and make the median of in [first, middle, last] pivot
        pre_process_median_pivot(input_list, low, high)
        partition_index = partition(input_list, low, high)
        comparison_count += high - low
        if partition_index > low:
            comparison_count += quicksort_with_median_pivot(input_list, low, partition_index - 1)
        if partition_index < high:
            comparison_count += quicksort_with_median_pivot(input_list, partition_index + 1, high)

        return comparison_count
    else:
        return 0
