import sys


class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def addneighbor(self, neighbor, cost=0):
        self.adjacent[neighbor] = cost

    def getConnections(self):
        return self.adjacent.keys()

    def getVertexName(self):
        return self.name

    def getCost(self, neighbor):
        return self.adjacent[neighbor]

    def setDistance(self, dis):
        self.distance = dis

    def getDistance(self):
        return self.distance

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visited = True


class Graph:
    def __init__(self, directed=False):
        self.VerDic = {}
        self.counts = 0
        self.directed = directed

    def __iter__(self):
        return iter(self.VerDic.values())

    def isDirected(self):
        return self.directed

    def vectexCount(self):
        return self.counts

    def addVertex(self, name):
        self.counts += 1
        vertex = Vertex(name)
        self.VerDic[name] = vertex
        return vertex

    def getVertex(self, name):
        if name in self.VerDic:
            return self.VerDic[name]
        else:
            return None

    def addEdge(self, frm, to, cost=0):
        if frm not in self.VerDic:
            self.addVertex(frm)
        if to not in self.VerDic:
            self.addVertex(to)
        self.VerDic[frm].addneighbor(self.VerDic[to], cost)
        if not self.directed:
            self.VerDic[to].addneighbor(self.VerDic[frm], cost)

    def getVertaxs(self):
        return self.VerDic.keys()

    def getEdges(self):
        edges = []
        for key, cur in self.VerDic.items():
            for nbr in cur.getConnections():
                curid = cur.getVertexName()
                nbrid = nbr.getVertexName()
                edges.append((curid, nbrid, cur.getCost(nbr)))
        return edges

    def getNeighbors(self, v):
        ver = self.VerDic[v]
        return ver.getConnections()
