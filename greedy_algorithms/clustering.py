# implementation by @kaba_y, https://korogba.github.io
# clustering algorithms using Kruskal's MST algorithm
from data_structures.union_find import UnionFind, UnionFindBitNode
from utils.file_operations import convert_file_to_kruskal_graph, convert_file_to_dict


# ToDo Write appropriate comment
def k_clustering(file_path, number_of_clusters) -> int:
    kruskal_graph = convert_file_to_kruskal_graph(file_path)
    union_find = UnionFind(kruskal_graph)
    partition_edges = []
    max_spacing = 0
    edge_count = 0

    while len(union_find) > number_of_clusters and edge_count < len(kruskal_graph.edge_list):
        edge = kruskal_graph.edge_list[edge_count]
        if not union_find.union(edge.node_one, edge.node_two):
            partition_edges.append(edge)
        edge_count += 1

    found_max = False
    for edge in kruskal_graph.edge_list[edge_count:]:
        if edge.node_one.parent != edge.node_two.parent:
            max_spacing = edge.weight
            found_max = True
            break
    if not found_max:
        # todo: sorted statement might have no effect. should assign return?
        sorted(partition_edges)
        max_spacing = partition_edges[0].weight

    print('Maximum spacing: ', max_spacing)
    return max_spacing


def get_cluster_nodes(node) -> set:
    search_nodes = set()
    node_value = [x for x in node.node_value]

    for i in range(len(node_value)):
        node_value[i] = 1 - node_value[i]
        node_hash = " ".join(str(item) for item in node_value)
        search_nodes.add(node_hash)

        for j in range((i + 1), len(node_value)):
            node_value[j] = 1 - node_value[j]
            node_hash = " ".join(str(item) for item in node_value)
            search_nodes.add(node_hash)
            node_value[j] = 1 - node_value[j]

        node_value[i] = 1 - node_value[i]

    return search_nodes


def spacing_count_with_hash(file_path) -> int:
    node_list = convert_file_to_dict(file_path)
    union_find = UnionFindBitNode(list(node_list.values()))

    for key, node in node_list.items():
        search_nodes = get_cluster_nodes(node)
        for search_node in search_nodes:
            if search_node in node_list:
                retrieved_node = node_list[search_node]
                union_find.union(node, retrieved_node)

    print('Spacing count: ', len(union_find))
    return len(union_find)
