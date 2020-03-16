import graph


class Solution:
    def __init__(self):
        self.visit = set()
        self.parent = {}

    def dfs(self, G: graph.Graph, node: graph.Vertex, target: graph.Vertex):
        node_name = node.getVertexName()
        if node == target:
            return self.parent
        if node_name not in self.visit:
            self.visit.add(node_name)
        for nbr in G.getNeighbors(node_name):
            nbr_name = nbr.getVertexName()
            if nbr_name not in self.visit:
                self.parent[nbr_name] = node_name
                self.dfs(G, nbr, target)
        return None
