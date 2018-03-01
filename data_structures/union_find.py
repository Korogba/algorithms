# implementation by @kaba_y, https://korogba.github.io
# Simple implementation of Union-Find data structure used in Kruskal's algorithm and clustering


class UnionFind:
    """
    Union find data structure to optimize Kruskal's algorithm
    """

    def __init__(self, kruskal_graph):
        self.partitions = {}
        for node in kruskal_graph.node_list:
            node.parent = node
            self.partitions[node] = [node.parent]

    @staticmethod
    def find(node_value):
        return node_value.parent

    def union(self, node_one, node_two) -> bool:
        parent_one = node_one.parent
        parent_two = node_two.parent

        if parent_one == parent_two:
            return False

        size_one = len(self.partitions.get(parent_one))
        size_two = len(self.partitions.get(parent_two))

        if size_one >= size_two:
            for node in self.partitions.get(parent_two):
                node.parent = parent_one
                self.partitions[parent_one].append(node)

            self.partitions.pop(parent_two)
        else:
            for node in self.partitions.get(parent_one):
                node.parent = parent_two
                self.partitions[parent_two].append(node)

            self.partitions.pop(parent_one)

        return True

    def __len__(self):
        return len(self.partitions)


class UnionFindBitNode:
    """
    Same as UnionFind but works with BitNode's
    todo: find way to use both
    """

    def __init__(self, node_list):
        self.partitions = {}
        for node in node_list:
            self.partitions[node] = [node.parent]

    @staticmethod
    def find(node_value):
        return node_value.parent

    def union(self, node_one, node_two) -> bool:
        parent_one = node_one.parent
        parent_two = node_two.parent

        if parent_one == parent_two:
            return False

        size_one = len(self.partitions.get(parent_one))
        size_two = len(self.partitions.get(parent_two))

        if size_one >= size_two:
            for node in self.partitions.get(parent_two):
                node.parent = parent_one
                self.partitions[parent_one].append(node)

            self.partitions.pop(parent_two)
        else:
            for node in self.partitions.get(parent_one):
                node.parent = parent_two
                self.partitions[parent_two].append(node)

            self.partitions.pop(parent_one)

        return True

    def __len__(self):
        return len(self.partitions)