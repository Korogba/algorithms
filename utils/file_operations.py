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
