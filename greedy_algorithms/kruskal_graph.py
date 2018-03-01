# implementation by @kaba_y, https://korogba.github.io
# Definition of components used in k-means clustering using Kruskal's algorithm
from bisect import bisect_left
from operator import xor


# ToDo Write appropriate comment
class KruskalNode:
    """
    Representation of a Vertex in a Kruskal graph.
    Use regular Node class?
    """

    def __init__(self, value):
        assert isinstance(value, int)

        self.node_value = value
        self.rank = 0
        self.parent = None

    def __eq__(self, other) -> bool:
        assert isinstance(other, KruskalNode)
        return self.node_value == other.node_value

    def __lt__(self, other) -> bool:
        assert isinstance(other, KruskalNode)
        return self.node_value < other.node_value

    def __hash__(self):
        return hash(self.node_value)


class KruskalEdge:
    """
    Representation of an Edge to in a Kruskal graph.
    """

    def __init__(self, node, neighbor, weight):
        assert isinstance(node, KruskalNode)
        assert isinstance(neighbor, KruskalNode)

        self.weight = weight
        self.node_one = node
        self.node_two = neighbor

    def __eq__(self, other) -> bool:
        assert isinstance(other, KruskalEdge)
        return (self.node_one == other.node_one and self.node_two == other.node_two) or \
               (self.node_one == other.node_two and self.node_two == other.node_one)

    def __lt__(self, other) -> bool:
        assert isinstance(other, KruskalEdge)
        return self.weight < other.weight

    def __hash__(self):
        return hash(self.node_one.node_value + self.node_two.node_value)


class KruskalGraph:
    """
    Representation of a graph as a sorted list of edges
    """

    def __init__(self):
        self.edge_list = []
        self.node_list = []

    def append(self, edge):
        index = bisect_left(self.edge_list, edge)

        if index != len(self.edge_list) and self.edge_list[index] == edge:
            return
        else:
            self.edge_list.insert(index, edge)

    def find_or_create(self, node_value) -> KruskalNode:
        new_node = KruskalNode(node_value)
        index = bisect_left(self.node_list, new_node)

        if index != len(self.node_list) and self.node_list[index] == new_node:
            return self.node_list[index]
        else:
            self.node_list.insert(index, new_node)
            return new_node

    def append_weighted_edges(self, node_value, neighbor_value, weight):
        node = self.find_or_create(node_value)
        neighbor = self.find_or_create(neighbor_value)
        edge = KruskalEdge(node, neighbor, weight)
        self.append(edge)


class BitNode:
    """
    Representation of a Vertex in a with values of bits.
    Use regular Node class?
    """

    def __init__(self, value):
        assert isinstance(value, list)
        self.node_value = value
        self.parent = self

    def __eq__(self, other) -> bool:
        assert isinstance(other, BitNode)
        return self.decimal() == other.decimal()

    def __hash__(self):
        return hash(self.decimal())

    def decimal(self) -> int:
        add_val = 0
        for bit in range(len(self.node_value)):
            add_val += (self.node_value[bit] * pow(2, bit))

        return add_val

    def distance(self, other):
        assert isinstance(other, BitNode)
        exclusive_or = [xor(x, y) for (x, y) in zip(self.node_value, other.node_value)]
        return sum(exclusive_or)