from graph_algorithms.graph_definition import GraphAsNodeList, Node
from collections import deque
from bisect import bisect_left

# Throws a RuntimeError: maximum recursion depth exceeded. ToDo: How to optimize to avoid this?
# https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
from utils import file_operations


def depth_first_search_recursive(graph, start_node) -> deque:
    assert isinstance(graph, GraphAsNodeList)
    assert isinstance(start_node, Node)

    visited_nodes = deque([start_node])
    start_node.visited = True

    for neighbor in start_node.edges:
        if not neighbor.visited:
            visited_nodes.extend(depth_first_search_recursive(graph, neighbor))

    return visited_nodes


def depth_first_search_iterative(graph, start_node) -> int:
    assert isinstance(graph, GraphAsNodeList)
    assert isinstance(start_node, Node)

    visited_nodes = deque()
    start_node.visited = True
    node_stack = [start_node]

    while node_stack:
        current_node = node_stack.pop()
        visited_nodes.append(current_node)
        for neighbor in current_node.edges:
            if not neighbor.visited:
                neighbor.visited = True
                neighbor.leader = start_node
                node_stack.append(neighbor)

    return len(visited_nodes)


def depth_first_search_iterative_reverse(graph, start_node, finishing_time) -> tuple:
    assert isinstance(graph, GraphAsNodeList)
    assert isinstance(start_node, Node)

    start_node.visited = True
    node_stack = [start_node]
    finishing_stack = []
    finished_nodes = []

    while node_stack:
        current_node = node_stack.pop()
        finishing_stack.append(current_node)
        if current_node.in_edges:
            i = 0
            for neighbor in current_node.in_edges:
                # keep count of un-visited nodes reached from current_node
                if not neighbor.visited:
                    i += 1
                    neighbor.visited = True
                    neighbor.parent = current_node
                    node_stack.append(neighbor)
            if i == 0:
                finishing_time = book_keeping_finishing_times(current_node, finished_nodes, finishing_stack,
                                                              finishing_time, node_stack)

        else:
            finishing_time = book_keeping_finishing_times(current_node, finished_nodes, finishing_stack,
                                                          finishing_time, node_stack)

    while finishing_stack:
        finishing_time = finishing_time + 1
        finished_node = finishing_stack.pop()
        finished_node.finishing_time = finishing_time
        finished_nodes.append(finished_node)

    return finishing_time, finished_nodes


def book_keeping_finishing_times(current_node, finished_nodes, finishing_stack, finishing_time, node_stack):
    # this means current_node is a dead end: move up along the parent and count finishing time
    finishing_time = finishing_time + 1
    current_node.finishing_time = finishing_time
    finished_nodes.append(current_node)
    finishing_stack.remove(current_node)
    if len(node_stack) > 0:
        while current_node.parent != node_stack[-1].parent:
            parent = current_node.parent
            finishing_time = finishing_time + 1
            parent.finishing_time = finishing_time
            finished_nodes.append(parent)
            finishing_stack.remove(parent)
            current_node = parent
    return finishing_time


def kosaraju_two_pass_algorithm(file_path) -> list:
    """
    - perform DFS with the edges reversed to get the finishing times of each node
    -
    :return:
    """
    my_graph = file_operations.convert_file_to_graph_as_node_list(file_path)
    t = 0
    print("Running...")
    top_five_scc_sizes = [0, 0, 0, 0, 0]
    finished_nodes = []

    for node in my_graph.node_list:
        if not node.visited:
            t, inner_finished_nodes = depth_first_search_iterative_reverse(my_graph, node, t)
            finished_nodes.extend(inner_finished_nodes)

    print("Done with first pass.")

    my_graph.clear()

    print("Graph cleared")

    while finished_nodes:
        node = finished_nodes.pop()
        if not node.visited:
            scc_size = depth_first_search_iterative(my_graph, node)
            if scc_size > top_five_scc_sizes[0]:
                i = bisect_left(top_five_scc_sizes, scc_size) - 1
                tmp = top_five_scc_sizes[i]
                top_five_scc_sizes[i] = scc_size
                while i > 0:
                    in_tmp = top_five_scc_sizes[i - 1]
                    top_five_scc_sizes[i - 1] = tmp
                    tmp = in_tmp
                    i = i - 1

    print("Done with second pass")

    return top_five_scc_sizes
