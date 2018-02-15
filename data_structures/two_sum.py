# implementation by @kaba_y, https://korogba.github.io
import multiprocessing
from multiprocessing.pool import Pool

from utils.file_operations import convert_file_to_dict_of_numbers

lower_limit = -10000
upper_limit = 10000


def two_sum(file_path) -> int:
    number_stream = convert_file_to_dict_of_numbers(file_path)
    number_of_target = 0

    for i in range(lower_limit, upper_limit + 1):
        for value in number_stream:
            target = i - value
            if target in number_stream and target != value:
                number_of_target += 1
                break

    return number_of_target


def two_sum_parallel(number_stream, target) -> int:
    number_of_target = 0

    for value in number_stream:
        offset = target - value
        if offset in number_stream and offset != value:
            number_of_target += 1
            break

    return number_of_target


# Demo to show parallelism
num_cores = multiprocessing.cpu_count()
numbers = convert_file_to_dict_of_numbers('2sum.txt')

number_range = tuple((numbers, x) for x in range(lower_limit, upper_limit + 1))

if __name__ == '__main__':
    with Pool(5) as p:
        print(sum(p.starmap(two_sum_parallel, number_range)))
