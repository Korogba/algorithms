# implementation by @kaba_y, https://korogba.github.io
from bisect import bisect_left
from collections import deque

from data_structures.huffman_node import HuffmanNode
from utils.file_operations import convert_file_to_huffman_list


def increment_count(node):
    if node.left_node is None and node.right_node is None:
        node.code_length += 1
        return

    increment_count(node.left_node)
    increment_count(node.right_node)


def merge_into(merged_nodes, nodes):
    first_node = nodes[0]
    second_node = nodes[1]

    merge_node = HuffmanNode(first_node.key + second_node.key)
    # todo: find better way
    increment_count(first_node)
    increment_count(second_node)
    merge_node.left_node = first_node
    merge_node.right_node = second_node

    index = bisect_left(merged_nodes, merge_node)
    merged_nodes.insert(index, merge_node)


def huffman_algorithm(file_path) -> []:
    """implement Huffman encoding for the given symbol frequencies in the file specified by file_path"""
    node_list = convert_file_to_huffman_list(file_path)
    merged_nodes = deque()

    while node_list:
        nodes = []
        while len(nodes) < 2:
            if node_list:
                if merged_nodes and merged_nodes[0] < node_list[0]:
                    nodes.append(merged_nodes.popleft())
                else:
                    nodes.append(node_list.popleft())
            else:
                if merged_nodes:
                    nodes.append(merged_nodes.popleft())

        merge_into(merged_nodes, nodes)

    while len(merged_nodes) > 1:
        first_node = merged_nodes.popleft()
        second_node = merged_nodes.popleft()
        merge_into(merged_nodes, [first_node, second_node])
    # todo: find better way: use bfs
    leaves = traverse(merged_nodes[0])
    sorted_leaves = sorted(leaves, key=lambda n: n.code_length)
    return sorted_leaves


# not used, yet!
def traverse(node) -> []:
    leaves = []
    if node.left_node is None and node.right_node is None:
        return [node]

    leaves.extend(traverse(node.left_node))
    leaves.extend(traverse(node.right_node))

    return leaves
