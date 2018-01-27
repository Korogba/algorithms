# implementation by @kaba_y, https://korogba.github.io
from random import sample


class Graph:
    """Representation of a graph as a dict of list"""

    def __init__(self, directed, a_list):
        assert isinstance(directed, bool)
        assert isinstance(a_list, dict)

        self.directed = directed
        self.adjacency_list = a_list

    def contract_edges(self):
        if len(self.adjacency_list) == 2:
            return

        random_nodes = sample(self.adjacency_list.keys(), 2)
        while True:
            if len([i for i in list(random_nodes[0]) if i in self.adjacency_list.get(random_nodes[1])]) > 0:
                break
            random_nodes = sample(self.adjacency_list.keys(), 2)

        node = random_nodes[0]
        neighbor = random_nodes[1]

        merged_node = node | neighbor

        merged_edges = [i for i in self.adjacency_list.get(node) + self.adjacency_list.get(neighbor)
                        if i not in merged_node]

        # delete nodes from adjacency_list
        del self.adjacency_list[node]
        del self.adjacency_list[neighbor]

        self.adjacency_list[merged_node] = merged_edges

        self.contract_edges()

