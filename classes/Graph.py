import time
class Graph:
    def __init__(self, file_path):
        self.adjacencyList = {}
        self.ReadFile(file_path)

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
        T.append((distance, father))
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
                if i in visited or i in Q:
                    continue
                T.append((distance, father))
                Q.append(i)
        return T
    
    def ReadFile(self,file_path):
        # Executando a leitura do db e armazenando em lines
        with open(file_path, "+r") as line:
            lines = line.readlines()

        # Tratando a lista lines para preencher de forma correta os vertices e arestas
        for line in lines:

            _, verticeA, verticeB, weight = line.split(" ")
            if verticeA in self.adjacencyList.keys():
               self.adjacencyList[verticeA].append((verticeB, weight))
            else:
               self.adjacencyList.update({verticeA: [(verticeB, weight)]})
            if verticeB in self.adjacencyList.keys():
               self.adjacencyList[verticeB].append((verticeA, weight))
            else:
               self.adjacencyList.update({verticeB: [(verticeA, weight)]})
