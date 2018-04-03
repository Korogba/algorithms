from multiprocessing.pool import Pool
from constraint_satisfaction.two_sat import papadimitriou

if __name__ == '__main__':
    sat_list = ['2sat1.txt', '2sat2.txt', '2sat3.txt', '2sat4.txt', '2sat5.txt', '2sat6.txt']
    with Pool(4) as p:
        print(p.map(papadimitriou, sat_list))

# def timing_function():
#     print("Done: ", tsp_with_nearest_distance_heuristics('nn.txt'))
#
#
# t = timeit.timeit("timing_function()", setup="from __main__ import timing_function", number=1)
# print("Time taken: ", t)

# Solution is: 26442.73030895475
# Time taken to run: 29362.99019825796
# def timing_function():
#     print("Done: ", tsp('tsp.txt'))
#
#
# t = timeit.timeit("timing_function()", setup="from __main__ import timing_function", number=1)
# print("Time taken: ", t)

# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(floyd_warshall_algorithm, ['g1.txt', 'g2.txt', 'g3.txt']))

# print(knapsack('knapsack1.txt'))

# bits = get_mwis('mwis.txt')
# print(bits)
# print(s)

# merged_nodes = huffman_algorithm('huffman.txt')
#
# print(merged_nodes[0].code_length, ' ', merged_nodes[len(merged_nodes) - 1].code_length)


# clustering_process = Process(target=k_clustering, args=('clustering1.txt', 4))
# count_process = Process(target=spacing_count_with_hash, args=('clustering_big.txt', ))
# clustering_process.start()
# count_process.start()

# kruskal_graph = convert_file_to_kruskal_graph('input_completeRandom_10_32.txt')
# union_find = UnionFind(kruskal_graph)
# [print(x.weight, '\t') for x in kruskal_graph.edge_list]

# from greedy_algorithms.prims_algorithm import prims_algorithm
#
# mst_cost = prims_algorithm('input_random_65_100000.txt')
# print("Cost of minimum spanning tree is: ", mst_cost)

# weighted_completion_time_difference = weighted_completion_time('jobs.txt', False)
#
# weighted_completion_time_quotient = weighted_completion_time('jobs.txt', True)
#
# print("Completion time(difference): ", weighted_completion_time_difference)
# print("Completion time(quotient): ", weighted_completion_time_quotient)


# num_cores = multiprocessing.cpu_count()
# lower_limit = -10000
# upper_limit = 10000
# number_stream = convert_file_to_dict_of_numbers('2sum.txt')
#
# number_range = tuple((number_stream, x) for x in range(lower_limit, upper_limit + 1))
#
# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(sum(p.starmap(two_sum_parallel, number_range)))

# print(two_sum('2sum.txt'))

# print(get_median('Median.txt'))
#
# from graph_algorithms import dijkstra
# from graph_algorithms.graph_definition import DijkstraNode
#
# visited_nodes = dijkstra.dijkstra_shortest_path('dijkstraData.txt')
#
# nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
#
# for node in nodes:
#     index = visited_nodes.index(DijkstraNode(node))
#
#     print('Distance to ', visited_nodes[index].node_value, '\tis:\t', visited_nodes[index].key)

# removed_node = remove_arbitrary_item(heap, 10)

# print('Removed item: ', removed_node.key)

# head = get_min(heap)
#
# while head.key != float('inf'):
#     print(head.key)
#     head = get_min(heap)

# list_custom = [17, 0, 15, 20, 1, 11, 18, 3, 12, 19, 5, 7, 13, 16, 4, 2, 14, 6, 10, 9, 8]

# list_custom = [2148, 9058, 7742, 3153, 6324, 609, 7628, 5469, 7017, 504]

# list_custom = [9, 1, 3, 5, 7, 4, 2, 6, 0, 8]

# list_custom = read_file_into_list('QuickSort.txt')

# millis = int(round(time.time() * 1000))
# print

# def test():
#     """Test function"""
#     my_graph = convert_file_to_graph_as_node_list('SCC.txt')
#     print(len(my_graph.node_list))
#
#
# t = timeit.timeit("test()", setup="from __main__ import test", number=5)
# print(t)

# print("Starting...")

# global_leaders = kosaraju_two_pass_algorithm('SCC.txt')

# global_leaders.sort()

# [print(x, '\n') for x in global_leaders]

# print("Done.")

# [print(x.node_value, '=>', x.finishing_time, '\n') for x in global_leaders]

# my_graph = convert_file_to_graph_as_node_list('SCC.txt')
#
# print(len(my_graph.node_list))

# millis = int(round(time.time() * 1000))
# print(millis)

# my_graph = GraphAsDict(False, a_list)

# my_graph.contract_edges()

# print(my_graph.adjacency_list)

# print(len(my_graph.adjacency_list))

# [print(x, '=>', y, '\n') for (x, y) in my_graph.adjacency_list.items()]

# [print('Length =>', len(y), '\n') for (x, y) in my_graph.adjacency_list.items()]

# print('Minimum cut is: ', random_contraction(my_graph))

# [print(edge_set) for edge_set in my_graph.edge_set]

# list_custom = read_file_into_list('QuickSort.txt')

# recursive_count = quicksort_with_median_pivot(list_custom, 0, (len(list_custom) - 1))

# [print(x, '\n') for x in list_custom]

# print('Recursive count: ', recursive_count, '\n')
# print('TestClass count: ', TestClass.global_count, '\n')

# Todo: handle ties in the implementation of merge sort(inversion) - inversion.py

# ToDo: handle ties in the implementation of quick sort - quicksort.py

# ToDo: modify karatsuba to use bit string operations - multiplication.py, link below
# https://codereview.stackexchange.com/questions/165215/karatsuba-algorithm-in-python/165220

# ToDo: implement closest pair algorithm

# ToDo: implement Strassen's algorithm for matrix multiplication

# ToDo: optimize quicksort to use tail recursion and solve dutch flag problem, link below
# https://en.wikipedia.org/wiki/Quicksort#Algorithm

# ToDo: implement selection problem: solved using a randomized & deterministic algorithm (not practical???)

# ToDo: implement heap sort

# ToDo: implement bubble sort

# ToDo: implement bucket sort - not comparison-based sorting, good for data with known distributions

# ToDo: implement counting sort - not comparison-based sorting, good for data that are known to be small integers

# ToDo: implement radix sort - not comparison-based, assumes data are integers and sorts using bit-representation

# ToDo: implement randomised contraction algorithm - minimum cut of a graph_algorithms, implement optimized ones as well

# ToDo: implement BFS for both directed and undirected graph

# ToDo: calculate connected components in an un-directed graph

# ToDo: implement DFS for graph by modifying DFS above to use a stack and recursive DFS as well

# ToDo: implement naive topological ordering

# ToDo: calculate strongly connected components in a directed graph: kosaraju

# ToDo: implement a binary search tree: with all the operations: min, max, successor, predecessor, select & rank,
# ordering, insertion, deletion, print out all elements using in-order traversal

# ToDo: implement Red Black trees, AVL trees or splay trees(quite interesting: self-adjusting trees), B-trees, B+ trees

# ToDo: Greedy algorithms: Solve scheduling problem

# ToDo: look up optimal branching problem

# ToDo: Check out MSTs - State of the Art

# ToDo: Implement Huffman'a algorithm using a two queue's and a sorting????

# ToDo: Implement Sequence Alignment using DP

# ToDo: Implement optimal BST's using DP: Be sure to look up the optimized version that reduces complexity to ^2 from ^3

# ToDo: Implementation of Bellman-Ford using depth-first search and predecessors' to calculate negative cost cycle

# ToDo: Implementation of Floyd-Warshall Algorithm

# ToDo: Implementation of Johnson's all-pair shortest path algorithm

# ToDO: Constraint satisfaction problems: 2 SAT problem, 3 SAT problem

# ToDo: Implement vertex cover problem using dynamic programming for trees

# ToDo: Look up maximum flow problem

# ToDo: Implement maximum cut problem

# ToDo: Random walks on non-negative integers: checkout!

# Both algorithms below are examples of Linear Programming: Optimization of linear functions over
# the intersection half-spaces: Simplex method, Convex programming? Integer Programming?
# ToDo: Stable matching: Gale-Shapley Proposal Algorithm!

# ToDo: Bi-partite matching reduces to maximum flow problem

# ToDo: Geometric problems: e.g closest pair problem. Convex-Hull problem

# ToDo: Bounded memory: streaming algorithms

# ToDo: Exploiting parallelism: map reduce & hadoop
