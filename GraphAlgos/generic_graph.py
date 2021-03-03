# Heather Fryling
# 3/3/2021
# A basic directed graph representation for implementing graph algos.

class DiGraph:
    graph = None

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = set({})

    def add_edge(self, start, end):
        if start not in self.graph.keys():
            self.add_vertex(start)
        if end not in self.graph.keys():
            self.add_vertex(end)
        self.graph[start].add(end)

    def __repr__(self):
        return "DiGraph{" + str(self.graph) + "}"

my_graph = DiGraph()
print(my_graph)
my_graph.add_vertex(1)
print(my_graph)
my_graph.add_edge(1, 2)
print(my_graph)