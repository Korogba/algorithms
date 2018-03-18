# implementation by @kaba_y, https://korogba.github.io
from bisect import bisect_left
from random import sample


class GraphAsDict:
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


class Node:
    """Representation of vertices of a graph"""

    def __init__(self, value):
        assert isinstance(value, int)

        self.node_value = value
        self.edges = []
        self.in_edges = []
        self.finishing_time = 0
        self.visited = False
        self.parent = None
        self.leader = None

    def __eq__(self, other) -> bool:
        return self.node_value == other.node_value

    def __lt__(self, other) -> bool:
        assert isinstance(other, Node)
        return self.node_value < other.node_value

    def add_edge(self, edge):
        self.edges.append(edge)

    def add_edges(self, edge_list):
        self.edges.extend(edge_list)


class GraphAsNodeList:
    """Representation of a graph as a list of Nodes"""

    def __init__(self):
        self.node_list = []

    def add_nodes(self, node_list):
        self.node_list.extend(node_list)

    def add_node(self, node):
        self.node_list.append(node)

    def find_or_create(self, val) -> Node:
        new_node = Node(val)
        index = bisect_left(self.node_list, new_node)

        if index != len(self.node_list) and self.node_list[index] == new_node:
            return self.node_list[index]
        else:
            self.node_list.insert(index, new_node)
            return new_node

    def append(self, node_value, edge_list):
        # did a benchmark test and the method below is a tad bit faster than the one commented
        # self.find_or_create(node_value).edges.append(self.find_or_create(edge_list))
        neighbors = []
        new_node = self.find_or_create(node_value)
        for val in edge_list:
            neighbor = self.find_or_create(val)
            neighbor.in_edges.append(new_node)
            neighbors.append(neighbor)
        new_node.edges.extend(neighbors)

    def clear(self):
        for node in self.node_list:
            node.visited = False
            node.finishing_time = 0
            node.parent = None


class DijkstraNode:
    """Representation of node with a 'key' property to be used in heaps included"""

    def __init__(self, value):
        assert isinstance(value, int)

        self.node_value = value
        self.edges = []
        self.parent = None
        self.key = float('inf')

    def __eq__(self, other) -> bool:
        return self.node_value == other.node_value

    def __lt__(self, other) -> bool:
        assert isinstance(other, DijkstraNode)
        return self.key < other.key


class Edge:
    """Representation of edges of a graph"""

    def __init__(self, head, tail, weight, directed):
        assert isinstance(head, DijkstraNode)
        assert isinstance(tail, DijkstraNode)
        assert isinstance(directed, bool)

        self.head = head
        self.tail = tail
        self.weight = weight
        self.directed = directed

    def __eq__(self, other) -> bool:
        assert isinstance(other, Edge)
        if self.directed:
            return self.head == other.head and self.tail == other.tail
        else:
            return (self.head == other.head and self.tail == other.tail) \
                   or (self.head == other.tail and self.tail == other.head)

    def __lt__(self, other) -> bool:
        assert isinstance(other, Edge)
        return self.weight < other.weight


class DijkstraGraph:
    """Representation of a graph as a list of DijkstraNode with Edges"""

    def __init__(self):
        self.node_list = []

    def find_or_create(self, val) -> DijkstraNode:
        new_node = DijkstraNode(val)

        node_values = [x.node_value for x in self.node_list]
        index = bisect_left(node_values, val)

        if index != len(self.node_list) and self.node_list[index] == new_node:
            return self.node_list[index]
        else:
            self.node_list.insert(index, new_node)
            return new_node

    def append_weighted_edges(self, node_value, neighbor_value, weight, directed):
        node = self.find_or_create(node_value)
        neighbor = self.find_or_create(neighbor_value)
        edge = Edge(node, neighbor, weight, directed)
        node.edges.append(edge)


class PrimGraph(DijkstraGraph):
    """
    Representation of a graph as a list of DijkstraNode with Edges
    Extends DijkstraGraph to give a different implementation of the append_weighted_edges
    """

    def __init__(self):
        super().__init__()

    def append_weighted_edges(self, node_value, neighbor_value, weight, directed):
        node = self.find_or_create(node_value)
        neighbor = self.find_or_create(neighbor_value)

        edge = Edge(node, neighbor, weight, directed)
        node.edges.append(edge)

        neighbor_edge = Edge(neighbor, node, weight, directed)
        neighbor.edges.append(neighbor_edge)


class FloydWarshallGraph:
    """Representation of a graph as a list of DijkstraNodes and Edges"""

    def __init__(self):
        self.node_list = []
        self.edge_list = []

    def find_or_create(self, val) -> DijkstraNode:
        new_node = DijkstraNode(val)

        node_values = [x.node_value for x in self.node_list]
        index = bisect_left(node_values, val)

        if index != len(self.node_list) and self.node_list[index] == new_node:
            return self.node_list[index]
        else:
            self.node_list.insert(index, new_node)
            return new_node

    def append_weighted_edges(self, node_value, neighbor_value, weight, directed):
        node = self.find_or_create(node_value)
        neighbor = self.find_or_create(neighbor_value)
        edge = Edge(node, neighbor, weight, directed)
        self.edge_list.append(edge)
        node.edges.append(edge)
