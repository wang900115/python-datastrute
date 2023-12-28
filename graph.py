
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u,v,weight):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}

        self.graph[u][v] = weight
        self.graph[u][v] = weight



    def print_graph(self):
        for node in self.graph:
            print(node,'->','->'.join(f'({neighbor} distance:{weight})' for neighbor , weight in self.graph[node].items()))

graph = Graph()
graph.add_edge('A','B',5)
graph.add_edge('A','C',3)
graph.add_edge('B','C',8)
graph.add_edge('C','D',2)
graph.print_graph()
