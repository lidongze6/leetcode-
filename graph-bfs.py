import graph
import collections


class Solution:
    def bfs(self, G: graph.Graph, start: graph.Vertex, target: graph.Vertex):
        visited = set()
        parent = {}
        queue = collections.deque
        queue.append(start)
        while queue:
            cur = queue.popleft()
            cur_name = cur.getVertexName()
            if cur == target:
                return parent
            else:
                for nbr in G.getNeighbors(cur_name):
                    nbr_name = nbr.getVertexName()
                    if nbr_name in visited: continue
                    visited.add(nbr_name)
                    parent[nbr_name] = cur_name
                    queue.append(nbr)
        return None
