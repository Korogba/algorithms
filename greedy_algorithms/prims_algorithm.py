# implementation by @kaba_y, https://korogba.github.io
from random import sample

from graph_algorithms import heap_utils
from utils.file_operations import convert_file_to_prim_graph


def cost(minimum_spanning_tree):
    """
    Get the cost of the minimum spanning tree
    :param minimum_spanning_tree: supplied MST
    :return: sum of the weight of all edges of the tree
    """
    total_edge_cost = 0

    for node in minimum_spanning_tree:
        if node.parent is None:
            continue

        parent_edge = [edge for edge in node.edges if edge.tail == node.parent]
        total_edge_cost += parent_edge[0].weight

    return total_edge_cost


def prims_algorithm(file_path) -> int:
    """
    Two invariants to maintain: the heap should contain the vertices in the frontier: vertices not yet added to the MST
    The key of each vertex in the frontier is the minimum of the weight of all crossing edge of that vertex
    See Dijkstra's shortest path Implementation
    """
    graph = convert_file_to_prim_graph(file_path)
    start_node = sample(graph.node_list, 1)[0]
    start_node.key = 0
    minimum_spanning_tree = []
    total_edge_cost = 0

    frontier = heap_utils.heapify(graph.node_list)

    while frontier:
        next_node = heap_utils.get_min(frontier)
        minimum_spanning_tree.append(next_node)

        total_edge_cost += next_node.key

        edges_to_frontier = [edge for edge in next_node.edges if edge.tail in frontier]

        for edge in edges_to_frontier:
            tail = edge.tail

            if edge.weight < tail.key:
                heap_utils.remove_arbitrary_item(frontier, frontier.index(tail))

                tail.key = edge.weight
                tail.parent = next_node

                heap_utils.insert_into_heap(frontier, tail)

    return total_edge_cost
