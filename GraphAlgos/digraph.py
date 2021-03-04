# Heather Fryling
# 3/3/2021
# A basic directed graph representation for implementing graph algos.

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

my_graph = DiGraph()
print(my_graph)
my_graph.add_vertex(1)
print(my_graph)
my_graph.add_edge(1, 2)
print(my_graph)
print(my_graph.vert_count)
print(my_graph.edge_count)