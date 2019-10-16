"""
Check if a given graph is tree or not.
"""
from algorithm.graph.graph import UndirectedGraph
from algorithm.graph.undirected_graph_cycle import isCycleUtil

"""
An undirected graph is a tree if it has following properties.
1)There is no cycle.
2)The graph is connected.
"""


def check_graph_tree(graph):
    visited = [False] * graph.size()
    if isCycleUtil(graph, 0, visited, -1):
        return False
    for v in visited:
        if not v:
            return False
    return True


if __name__ == '__main__':
    graph = UndirectedGraph()
    graph.add_edge(1, 0)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(3, 4)
    print(check_graph_tree(graph))

    graph1 = UndirectedGraph()
    graph1.add_edge(1, 0)
    graph1.add_edge(0, 2)
    graph1.add_edge(2, 1)
    graph1.add_edge(0, 3)
    graph1.add_edge(3, 4)
    print(check_graph_tree(graph1))
