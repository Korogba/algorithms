# implementation by @kaba_y, https://korogba.github.io
from graph_algorithms import heap_utils
from utils.file_operations import convert_file_to_stream_of_numbers


def get_median(file_path) -> int:
    number_stream = convert_file_to_stream_of_numbers(file_path)
    low_heap = []
    high_heap = []
    medians = []

    for number in number_stream:
        low = heap_utils.peek_min(low_heap)
        high = heap_utils.peek_min(high_heap)

        if not low and not high:
            heap_utils.insert_into_heap(high_heap, number)
            medians.append(number)
        else:
            if number > high:
                heap_utils.insert_into_heap(high_heap, number)
            else:
                heap_utils.insert_into_heap(low_heap, -number)

            if abs(len(high_heap) - len(low_heap)) > 1:
                if len(high_heap) > len(low_heap):
                    high_min = heap_utils.get_min(high_heap)
                    heap_utils.insert_into_heap(low_heap, -high_min)
                    medians.append(-heap_utils.peek_min(low_heap))
                else:
                    low_max = heap_utils.get_min(low_heap)
                    heap_utils.insert_into_heap(high_heap, -low_max)
                    medians.append(-heap_utils.peek_min(low_heap))
            else:
                if len(high_heap) > len(low_heap):
                    medians.append(heap_utils.peek_min(high_heap))
                else:
                    medians.append(-heap_utils.peek_min(low_heap))

    return sum(medians) % 10000



