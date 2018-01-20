# implementation by @kaba_y, https://korogba.github.io
from math import log

from graph_algorithms.graph_definition import Graph
from copy import deepcopy

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


# ToDo: Use multi-threading, find optimization points! Too slow!
def random_contraction(graph_instance) -> int:
    assert isinstance(graph_instance, Graph)

    number_of_trials = int(pow(len(graph_instance.adjacency_list.keys()), 2)
                           * log(len(graph_instance.adjacency_list.keys())))
    minimum_cut = int(pow(len(graph_instance.adjacency_list.keys()), 2))

    for unused in range(10000):
        mutated_graph = deepcopy(graph_instance)
        while len(mutated_graph.adjacency_list) > 2:
            mutated_graph.contract_edge()
        current_cut_count = count_cut(graph_instance, mutated_graph)
        if current_cut_count < minimum_cut:
            minimum_cut = current_cut_count

    return minimum_cut


def count_cut(graph_instance, mutated_graph) -> int:
    assert isinstance(graph_instance, Graph)
    assert isinstance(mutated_graph, Graph)
    assert len(mutated_graph.adjacency_list) == 2, 'Invalid parameters supplied'

    # for each item in the key in the adjacency list of the mutated graph
    # get its' original neighbors from graph instance
    # count the number of neighbors in the value
    for key, value in mutated_graph.adjacency_list.items():
        cut_count = 0
        key_values = list(key)
        edge_values = set(edge for edge_set in value for edge in edge_set)
        for item in key_values:
            item_neighbor = set(item_edge for item_edge_set in graph_instance.adjacency_list.get(frozenset({item}))
                                for item_edge in item_edge_set)
            cut_count += len(edge_values & item_neighbor)
        # return early to avoid double additions
        return cut_count
