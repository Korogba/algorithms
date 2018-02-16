# by @kaba_y, https://korogba.github.io
from bisect import bisect_left
from typing import Optional

from graph_algorithms.graph_definition import GraphAsNodeList, DijkstraGraph, PrimGraph
from greedy_algorithms.job_definition import JobQuotient, JobDifference


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


def convert_file_to_graph_as_dict(file_path) -> dict:
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


def convert_file_to_graph_as_node_list(file_path) -> Optional[GraphAsNodeList]:
    """
    Read the numbers on each line in the file provided and get the nodes represented by the first and second columns
    Update the edge list of the first node to include the second node
    :param file_path: relative/full path to the file containing the list of directed edges on new lines
    :return: a graph representing the content of the file as a list of nodes
    """

    try:
        graph = GraphAsNodeList()

        node_list = convert_file_to_graph_for_scc(file_path)
        [graph.append(x, y) for x, y in node_list.items()]
        # did a benchmark test and the method above is a tad bit faster
        # lines = [line.rstrip('\n') for line in open(file_path, 'r')]
        # [graph.append(int(x), int(y)) for x, y in (split_line.split() for split_line in lines)]

        return graph
    except IOError:
        print('Unable to open file:', file_path)
        return None


def convert_file_to_graph_for_scc(file_path) -> dict:
    """
    Read the numbers on each line in the file provided and get the nodes represented by the first and second columns
    Update the edge list of the first node to include the second node
    :param file_path: relative/full path to the file containing the list of directed edges on new lines
    :return: a graph representing the content of the file as a list of nodes
    """

    try:
        node_dict = {}
        lines = [line.rstrip('\n') for line in open(file_path, 'r')]

        for each_line in lines:
            x, y = each_line.split()
            if int(x) not in node_dict.keys():
                node_dict[int(x)] = [int(y)]
            else:
                node_dict[int(x)].append(int(y))

        return node_dict
    except IOError:
        print('Unable to open file:', file_path)
        return {}


def convert_file_to_adjacency_list_for_dijkstra(file_path) -> Optional[DijkstraGraph]:
    """
    Iterate over the list of, for each line create a node and add the edges
    """

    try:
        graph = DijkstraGraph()
        lines = [line.rstrip('\n') for line in open(file_path, 'r')]
        for each_line in lines:
            adjacency_list = each_line.split()
            node_value = int(adjacency_list[0])
            [graph.append_weighted_edges(node_value, int(edge), int(weight), False)
             for edge, weight in (item.split(',') for item in adjacency_list[1:])]
        return graph
    except IOError:
        print('Unable to open file:', file_path)
        return None


def convert_file_to_stream_of_numbers(file_path) -> list:
    """
    Break up file into list of numbers
    """

    try:
        return [int(line.rstrip('\n')) for line in open(file_path, 'r')]
    except IOError:
        print('Unable to open file:', file_path)
        return []


def convert_file_to_dict_of_numbers(file_path) -> set:
    """
    Add each number in the file to a set
    """

    try:
        return set(int(line.rstrip('\n')) for line in open(file_path, 'r'))
    except IOError:
        print('Unable to open file:', file_path)
        return set()


def convert_file_to_jobs(file_path, is_score_quotient) -> list:
    """
    Add each number in the file to a set
    """

    try:
        jobs = []
        lines = [line.rstrip('\n') for line in open(file_path, 'r')]
        for each_line in lines[1:]:
            job_values = each_line.split()

            if is_score_quotient:
                new_job = JobQuotient(int(job_values[0]), int(job_values[1]))
            else:
                new_job = JobDifference(int(job_values[0]), int(job_values[1]))

            index = bisect_left(jobs, new_job)
            jobs.insert(index, new_job)

        return jobs
    except IOError:
        print('Unable to open file:', file_path)
        return []


def convert_file_to_adjacency_list_for_prim(file_path) -> Optional[PrimGraph]:
    """
    Iterate over the list of, for each line create a node and add the edges
    Similar to: convert_file_to_adjacency_list_for_dijkstra
    """

    try:
        graph = PrimGraph()
        lines = [line.rstrip('\n') for line in open(file_path, 'r')]

        for each_line in lines[1:]:
            adjacency_list = each_line.split()
            node_value = int(adjacency_list[0])
            neighbor_value = int(adjacency_list[1])
            weight = int(adjacency_list[2])
            graph.append_weighted_edges(node_value, neighbor_value, weight, False)

        return graph
    except IOError:
        print('Unable to open file:', file_path)
        return None
