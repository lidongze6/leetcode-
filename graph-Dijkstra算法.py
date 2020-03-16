import sys
import graph
import heapq


class Solution:
    def Dijkstra(self, G: graph.Graph, start: graph.Vertex):
        visited = set()
        parents = {start.getVertexName(): None}
        stack = [(0, start)]
        distance = {start.getVertexName(): 0}
        while stack:
            tmp = heapq.heappop()
            name = tmp[1].getVertexName()
            visited.add(name)
            nbr = G.getNeighbors(name)
            for node in nbr:
                node_name = node.getVertexName()
                if node_name in visited:
                    continue
                else:
                    node_dis = node.getCost(tmp[1]) + distance[name]
                    if node_dis < distance.get(node_name, sys.maxsize):
                        heapq.heappush(stack, (node_dis, node))
                        parents[node_name] = name
                        distance[node_name] = node_dis
        return parents, distance
