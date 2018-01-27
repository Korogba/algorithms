# by @kaba_y, https://korogba.github.io


def read_file_into_list(file_path) -> list:
    """
    Read the number on each line in the file provided and return a list containing the number
    :param file_path: relative/full path to the file containing the list of numbers separated by new lines
    :return: a list containing each number (as an int) read from the file or an empty list if file cannot be found/read
    """

    try:
        file_object = open(file_path, 'r')
    except IOError:
        print('Unable to open file:', file_path)
        return []
    else:
        with file_object:
            number_list = file_object.read().splitlines()
            number_list = list(map(int, number_list))

    return number_list


def break_up_line_into_arr(line) -> tuple:
    line_array = line.split()
    line_array = [int(x) for x in line_array]

    return frozenset(line_array[:1]), line_array[1:]


def get_adjacency_list_from_array(lines) -> list:
    return [break_up_line_into_arr(x) for x in lines]


def convert_file_to_graph(file_path) -> dict:
    """
    Read the numbers on each line in the file provided and create a dict pair with the first number as the key and
    successive numbers in a set as value
    :param file_path: relative/full path to the file containing the list of numbers separated by new lines
    :return: a dict representing the content of the file as key(vertex):value(set of adjacent vertices) pairs
    """

    try:
        lines = [line.rstrip('\n') for line in open(file_path, 'r')]
        return {node: neighbors for (node, neighbors) in get_adjacency_list_from_array(lines)}
    except IOError:
        print('Unable to open file:', file_path)
        return {}
