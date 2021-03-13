# Heather Fryling
# 3/3/2021
# A basic directed graph in adjacency list representation for implementing 
# graph algos.

class DiGraph:
    def __init__(self):
        self.graph = {}
        self.vert_count = 0
        self.edge_count = 0

    def add_vertex(self, vertex):
        self.graph[vertex] = set({})
        self.vert_count += 1

    def add_edge(self, start, end):
        if start not in self.graph.keys():
            self.add_vertex(start)
        if end not in self.graph.keys():
            self.add_vertex(end)
        self.graph[start].add(end)
        self.edge_count += 1

    def remove_edge(self, start, end):
        self.graph[start].remove(end)
        self.edge_count -= 1

    def remove_vertex(self, vertex):
        if vertex not in self.graph.keys():
            return
        for _ in self.graph[vertex]:
            self.edge_count -= 1
        for v in self.graph.keys():
            for item in self.graph[v]:
                if item == vertex:
                    self.graph[v].remove(vertex)
                    self.edge_count -= 1
        self.graph.pop(vertex, None)

    def __repr__(self):
        return "DiGraph{" + str(self.graph) + "}"

    def __eq__(self, object):
        if isinstance(object, DiGraph) and object.graph == self.graph:
            return True
        return False

# my_graph = DiGraph()
# print(my_graph)
# my_graph.add_vertex(1)
# print(my_graph)
# my_graph.add_edge(1, 2)
# print(my_graph)
# print(my_graph.vert_count)
# print(my_graph.edge_count)

# eq_graph = DiGraph()
# eq_graph.add_edge(1, 2)
# print(my_graph == my_graph)
# print(my_graph == eq_graph)

# empty_graph = DiGraph()
# print(my_graph == empty_graph)

# other_graph = DiGraph()
# other_graph.add_edge(1, 2)
# other_graph.add_edge(3, 4)
# print(my_graph == other_graph)

# print(my_graph == "not_a_graph")