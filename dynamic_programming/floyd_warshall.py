# implementation by @kaba_y, https://korogba.github.io
from typing import Optional

from utils.file_operations import convert_file_to_floyd_warshall_graph


def floyd_warshall_algorithm(file_path) -> Optional[int]:
    graph = convert_file_to_floyd_warshall_graph(file_path)
    solution = {}
    n = len(graph.node_list)

    # initialize zero-th k's
    for i in range(n):
        current_node = graph.node_list[i]
        edges = current_node.edges
        for j in range(n):
            if i == j:
                solution[(i, j, 0)] = 0
            else:
                edge_exists = False
                current_neighbor = graph.node_list[j]
                for edge in edges:
                    if current_neighbor == edge.tail:
                        solution[(i, j, 0)] = edge.weight
                        edge_exists = True
                        break
                if not edge_exists:
                    solution[(i, j, 0)] = float('inf')
    # perform recurrence
    # only use previous solutions for k to prevent out_of_memory - SIGKILL
    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                solution[(i, j, 1)] = min(solution[(i, j, 0)],
                                          (solution[i, k, 0] + solution[k, j, 0]))

                if i == j and k == (n - 1) and solution[(i, j, 1)] < 0:
                    # return None on detecting negative cost cycle
                    return None

                solution[(i, j, 0)] = solution[(i, j, 1)]

    # get all shortest paths
    shortest_paths = [solution[(i, j, 0)] for i in range(n) for j in range(n)]
    # return minimum shorted path
    return min(shortest_paths)
