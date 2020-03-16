import graph


class Solution:
    def dfs(self, G: graph.Graph, start: graph.Vertex, target: graph.Vertex):
        stack = [start]
        visited = set()
        parent = {}
        while stack:
            cur = stack.pop()
            if cur.getVertexName() == target.getVertexName():
                return parent
            else:
                nbr = G.getNeighbors(cur.getVertexName())
                for node in nbr:
                    name = node.getVertexName()
                    if name not in visited:
                        visited.add(name)
                        parent[name] = cur.getVertexName()
                        stack.append(node)
        return -1
