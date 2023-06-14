MAX_SIZE = 10000000000000000000000000000000000000000000
class Graph:
    def __init__(self, filePath=str):
        self.adjacencyList = {}
        self.ReadFile(filePath)

    def verifyVertice(self, vertice):
        return vertice in self.adjacencyList.keys()

    def ReadFile(self, filePath):
        # Executando a leitura do db e armazenando em lines
        with open(filePath, "+r") as line:
            lines = line.readlines()

        # Tratando a lista lines para preencher de forma correta os vertices e arestas
        for line in lines:

            _, verticeA, verticeB, weight = line.split(" ")
            weight = int(weight)
            if verticeA in self.adjacencyList.keys():
                self.adjacencyList[verticeA].append((verticeB, weight))
            else:
                self.adjacencyList.update({verticeA: [(verticeB, weight)]})
            if verticeB in self.adjacencyList.keys():
                self.adjacencyList[verticeB].append((verticeA, weight))
            else:
                self.adjacencyList.update({verticeB: [(verticeA, weight)]})

    def showGraph(self):
        for vertice in self.adjacencyList.keys():
            print(f"{vertice}: {self.neighbor(vertice)}")

    def writeAdjacencyList(self, fileName):
        with open(f"db/{fileName}_AdjacencyList.txt", "+w") as file:
            for vertice in self.adjacencyList.keys():
                file.write(f"{vertice}: {self.neighbor(vertice)}\n")

    def n(self):
        return len(self.adjacencyList.keys())

    def m(self):
        edges = set()
        for edge in self.adjacencyList.values():
            for item in edge:
                edges.add(item)
        return len(edges)

    def neighbor(self, vertice):
        neighbor = set()
        for i in self.adjacencyList[vertice]:
            neighbor.add(i)
        return neighbor

    def d(self, vertice):
        return len(self.neighbor(vertice))

    def minD(self):
        return min([self.d(keys) for keys in self.adjacencyList.keys()])

    def maxD(self):
        return max([self.d(keys) for keys in self.adjacencyList.keys()])

    def bfs(self, vertice):

        distance, father = 0, None
        d, fathers = {}, {}
        visited, Q = set(), []
        d[vertice] = 0
        fathers[vertice] = None
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
                d[i] = distance
                fathers[i] = father
                Q.append(i)
        return d, fathers

    def dfs(self, vertice):
        visited, temp, father = set(), 0, None
        initTime, endTime, fathers, Q = {}, {}, {}, []
        Q.append(vertice)

        while Q:
            vert = Q.pop(0)
            if vert not in visited:
                visited.add(vert)
                temp += 1
                initTime[vert] = temp
                fathers[vert] = father
                neighbors = self.neighbor(vert)
                father = vert
                for i, _ in neighbors:
                    if i not in visited and i not in Q:
                        Q.append(i)
        for vert in visited:
            endTime[vert] = temp
            temp += 1

        return initTime, endTime, fathers

    def BellmanFord(self, vertice):
        # inicializando os dicionarios com as distâncias e predecessores
        d, father = {}, {}
        [d.update({vertice: MAX_SIZE}) for vertice in self.adjacencyList.keys()]
        [father.update({vertice: None})
         for vertice in self.adjacencyList.keys()]

        d[vertice] = 0
        father[vertice] = None

        while True:
            if not self.relaxStep(d, father, vertice):
                break
        for vertice in self.adjacencyList.keys():
            neighbors = self.neighbor(vertice)
            for neighbor, weight in neighbors:
                if d[neighbor] > d[vertice] + weight:
                    return None, None, "Negative cicles detect"
        return d, father, None

    def relaxStep(self, d, father, first):
        verifyChange = False        
        neighbors = self.neighbor(first)
        for neighbor, weight in neighbors:
            if d[neighbor] > d[first]+weight:
                d[neighbor] = d[first] + weight
                father[neighbor] = first

        for vertice in self.adjacencyList.keys():
            neighbors = self.neighbor(vertice)
            for neighbor, weight in neighbors:
                if d[neighbor] > d[vertice]+weight:
                    d[neighbor] = d[vertice] + weight
                    father[neighbor] = vertice
                    verifyChange = True
        return verifyChange
        
    
