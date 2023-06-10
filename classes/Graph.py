import time
class Graph:
    def __init__(self, adjacencyList=dict):
        self.adjacencyList = adjacencyList

    def n(self):
        return len(self.adjacencyList.keys())

    def m(self):
        count = 0
        for edge in self.adjacencyList.values():
            count += len(edge)
        return count

    def neighbor(self, vertice):
        return self.adjacencyList[vertice]

    def d(self, vertice):
        return len(self.adjacencyList[vertice])

    def minD(self):
        return min([len(value) for value in self.adjacencyList.values()])

    def maxD(self):
        return max(len(value) for value in self.adjacencyList.values())

    def bfs(self, vertice):

        distance, father = 0, None
        T = []
        visited, Q = set(), []
        Q.append(vertice)

        while Q:
            vert = Q.pop(0)
            if vert in visited:
                continue
            visited.add(vert)
            distance += 1
            father = vert
            neighbor = self.neighbor(vert)
            for i, _ in neighbor:
                if i in visited:
                    continue
                T.append((distance, father))
                Q.append(i)
        return T
