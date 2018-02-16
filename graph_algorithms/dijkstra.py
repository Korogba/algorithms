# implementation by @kaba_y, https://korogba.github.io
from graph_algorithms import heap_utils
from utils.file_operations import convert_file_to_adjacency_list_for_dijkstra


def dijkstra_shortest_path(file_path) -> list:
    """
    Two invariants to maintain: the heap should contain the vertices in the frontier of the search
    The key of each vertex in the frontier is the Dijkstra's number
    In other words the minimum of the sum of the weight of crossing edge and the Dijkstra's number of the vertex in the
    visited nodes
    """
    graph = convert_file_to_adjacency_list_for_dijkstra(file_path)
    start_node = graph.node_list[0]
    start_node.key = 0
    visited_nodes = []

    frontier = heap_utils.heapify(graph.node_list)

    while frontier:
        next_node = heap_utils.get_min(frontier)
        visited_nodes.append(next_node)

        edges_to_frontier = [edge for edge in next_node.edges if edge.tail in frontier]

        for edge in edges_to_frontier:
            tail = edge.tail

            if next_node.key + edge.weight < tail.key:
                heap_utils.remove_arbitrary_item(frontier, frontier.index(tail))

                tail.key = next_node.key + edge.weight
                tail.parent = next_node

                heap_utils.insert_into_heap(frontier, tail)
    return visited_nodes

