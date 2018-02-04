# implementation by @kaba_y, https://korogba.github.io
from graph_algorithms.graph_definition import DijkstraNode


def insert_into_heap(heap_items, node):
    """
    :param heap_items: array representation of a heap
    :param node: Dijkstra's node to insert
    :return: Nothing. Makes modifications in-place. 'un'-Functional programming? :(
    """
    heap_items.append(node)
    bubble_up(heap_items)


def get_min(heap_items) -> DijkstraNode:
    minimum_node = heap_items[0]
    heap_items[0] = heap_items[len(heap_items) - 1]
    del heap_items[len(heap_items) - 1]

    bubble_down(heap_items)
    return minimum_node


def bubble_down(heap_items, parent_index=0):
    """
    Keep moving parent at the top of the list till it gets to it's proper position
    :param parent_index: index to bubble down from
    :param heap_items:
    :return: NADA as in nothing: done in-place
    """
    left_child_index = (2 * parent_index) + 1
    right_child_index = (2 * parent_index) + 2

    while left_child_index < len(heap_items):
        if right_child_index < len(heap_items) and heap_items[right_child_index].key < heap_items[left_child_index].key\
                and heap_items[right_child_index].key < heap_items[parent_index].key:

            temp = heap_items[right_child_index]
            heap_items[right_child_index] = heap_items[parent_index]
            heap_items[parent_index] = temp

            parent_index = right_child_index
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2

        elif heap_items[left_child_index].key < heap_items[parent_index].key:
            temp = heap_items[left_child_index]
            heap_items[left_child_index] = heap_items[parent_index]
            heap_items[parent_index] = temp

            parent_index = left_child_index
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2

        else:
            break


def bubble_up(heap_items, node_index=-1):
    """
    Keep moving item at end of list up til it gets to it's proper location
    :param node_index: index to bubble up from
    :param heap_items: binary heap as an array
    :return: NADA as in nothing: done in-place
    """
    node_index = len(heap_items) - 1 if node_index == -1 else node_index
    parent_index = int((node_index - 1) / 2)

    while heap_items[node_index].key < heap_items[parent_index].key:
        temp = heap_items[parent_index]
        heap_items[parent_index] = heap_items[node_index]
        heap_items[node_index] = temp
        node_index = parent_index
        parent_index = int((node_index - 1) / 2)


def heapify(node_list) -> list:
    """
    Traverse through the list and create a binary heap represented as an array of the items in the list
    :param node_list: must have at least one item
    :return:
    """
    heap_items = []

    for node in node_list:
        insert_into_heap(heap_items, node)

    return heap_items


def remove_arbitrary_item(heap_items, index) -> DijkstraNode:
    removed_node = heap_items[index]
    heap_items[index] = heap_items[len(heap_items) - 1]

    del heap_items[len(heap_items) - 1]

    if len(heap_items) <= 1:
        return removed_node

    index = index - 1 if index == len(heap_items) and len(heap_items) > 0 else index
    parent_index = int((index - 1) / 2)

    if heap_items[index].key < heap_items[parent_index].key:
        bubble_up(heap_items, index)
    else:
        bubble_down(heap_items, index)

    return removed_node
