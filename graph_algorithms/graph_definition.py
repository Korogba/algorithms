# implementation by @kaba_y, https://korogba.github.io
from random import sample


class Graph:
    """Representation of a graph as a dict of sets"""

    def __init__(self, directed, a_list):
        assert isinstance(directed, bool)
        assert isinstance(a_list, dict)

        self.directed = directed
        self.adjacency_list = a_list
        # self.node_set = set((frozenset({node})) for node in a_list.keys())
        # self.edge_set = set((frozenset({node}), frozenset({neighbor}))
        #                     for node in a_list.keys() for neighbor in a_list.get(node))
        # self.edge_count = len(self.edge_set) if directed else len(self.edge_set) / 2

    def contract_edge(self):
        edge_set = set((node, neighbor)
                       for node in self.adjacency_list.keys() for neighbor in self.adjacency_list.get(node))
        selected_edge = sample(edge_set, 1)
        assert isinstance(selected_edge[0], tuple)
        node, neighbor = selected_edge[0]

        # merge the two set of nodes joined by the selected edge and update adjacency_list
        assert isinstance(neighbor, frozenset)
        assert isinstance(node, frozenset)
        merged_node = node | neighbor

        # merge the edge_set of the two nodes
        first_edge_set = self.adjacency_list.get(node)
        second_edge_set = self.adjacency_list.get(neighbor)
        merged_edges = (first_edge_set | second_edge_set) - {node, neighbor}

        # delete nodes from adjacency_list
        del self.adjacency_list[node]
        del self.adjacency_list[neighbor]

        # update each node that is adjacent to any item in the new node:
        # remove all entries and replace with merged_edges
        # if a any value from the merged node is contained in an adjacent node, delete such node:
        # mark that key as pointing to merged node and update the value list as such
        # continue iterating over values and remove further values found.
        for key, value in self.adjacency_list.items():
            if key == merged_node:
                continue
            add_merged_node = False
            delete_items = set()
            for item in value:
                if len(item & node) > 0 or len(item & neighbor) > 0:
                    add_merged_node = True
                    delete_items.add(item)
            if add_merged_node:
                new_edge_set = value - {node, neighbor}
                for del_item in delete_items:
                    new_edge_set = new_edge_set - del_item
                new_edge_set.add(merged_node)
                self.adjacency_list[key] = new_edge_set

        # update adjacency_list with the new node and edges
        self.adjacency_list[merged_node] = merged_edges

        # remove the selected nodes
        # self.node_set.remove(frozenset(node))
        # self.node_set.remove(frozenset(neighbor))
        # add the union of the nodes to the set
        # self.node_set.add(frozenset(merged_node))
