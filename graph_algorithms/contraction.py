# implementation by @kaba_y, https://korogba.github.io
from math import log

from graph_algorithms.graph_definition import Graph
from copy import deepcopy


def random_contraction(graph_instance) -> float:
    assert isinstance(graph_instance, Graph)

    number_of_trials = int(pow(len(graph_instance.adjacency_list.keys()), 2)
                           * log(len(graph_instance.adjacency_list.keys())))

    minimum_cut = float('inf')

    # You might want to use a lower number than n^2 * log(n) for speedy results
    for unused in range(number_of_trials):
        mutated_graph = deepcopy(graph_instance)
        mutated_graph.contract_edges()
        key, value = mutated_graph.adjacency_list.popitem()
        current_cut = len(value)

        if current_cut < minimum_cut:
            minimum_cut = current_cut

    return minimum_cut
