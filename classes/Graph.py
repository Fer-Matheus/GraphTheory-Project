import heapq

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

        distance, parent = 0, None
        d, parents = {}, {}
        visited, Q = set(), []
        d[vertice] = 0
        parents[vertice] = None
        Q.append(vertice)

        while Q:
            vert = Q.pop(0)
            if vert in visited:
                continue
            visited.add(vert)
            distance += 1
            parent = vert
            neighbor = self.neighbor(vert)
            for i, _ in neighbor:
                if i in visited or i in Q:
                    continue
                d[i] = distance
                parents[i] = parent
                Q.append(i)
        return d, parents

    def dfs(self, vertice):
        visited, temp, parent = set(), 0, None
        initTime, endTime, parents, Q = {}, {}, {}, []
        Q.append(vertice)

        while Q:
            vert = Q.pop(0)
            if vert not in visited:
                visited.add(vert)
                temp += 1
                initTime[vert] = temp
                parents[vert] = parent
                neighbors = self.neighbor(vert)
                parent = vert
                for i, _ in neighbors:
                    if i not in visited and i not in Q:
                        Q.append(i)
        for vert in visited:
            endTime[vert] = temp
            temp += 1

        return initTime, endTime, parents

    def BellmanFord(self, vertice):
        # inicializando os dicionarios com as distâncias e predecessores
        d, parent = {}, {}
        [d.update({vertice: MAX_SIZE}) for vertice in self.adjacencyList.keys()]
        [parent.update({vertice: None})
         for vertice in self.adjacencyList.keys()]

        d[vertice] = 0
        parent[vertice] = None

        while True:
            if not self.relaxStep(d, parent, vertice):
                break
        for vertice in self.adjacencyList.keys():
            neighbors = self.neighbor(vertice)
            for neighbor, weight in neighbors:
                if d[neighbor] > d[vertice] + weight:
                    return None, None, "Negative cicles detect"
        return d, parent, None

    def relaxBF(self, d, parent, first):
        verifyChange = False        
        neighbors = self.neighbor(first)
        for neighbor, weight in neighbors:
            if d[neighbor] > d[first]+weight:
                d[neighbor] = d[first] + weight
                parent[neighbor] = first

        for vertice in self.adjacencyList.keys():
            neighbors = self.neighbor(vertice)
            for neighbor, weight in neighbors:
                if d[neighbor] > d[vertice]+weight:
                    d[neighbor] = d[vertice] + weight
                    parent[neighbor] = vertice
                    verifyChange = True
        return verifyChange
    
    def Dijkstra(self, vertice):
        d, parent, Q , visited = {}, {}, [], set()
        [d.update({vert: MAX_SIZE})for vert in self.adjacencyList.keys()]
        [parent.update({vert: None}) for vert in self.adjacencyList.keys()]

        d[vertice] = 0
        heapq.heappush(Q,(vertice, 0))
        """
            vert = A
            A : (C,B)
            Q = B, B
            visited = C, A
        """
        while Q:
            vert, w = heapq.heappop(Q) # B 
            if vert in visited:
                continue
            visited.add(vert) # 
            self.relaxDijkstra(d,parent, vert)
            neighbors = self.neighbor(vert)
            for neighbor, weight in neighbors:
                if neighbor in visited or neighbor in Q:
                    continue
                heapq.heappush(Q,(neighbor, weight+w))

        return d, parent


    def relaxDijkstra(self, d, parent,vertice):
        neighbors = self.neighbor(vertice)
        for neighbor, weight in neighbors:
            if d[neighbor] > d[vertice] + weight:
                d[neighbor] = d[vertice] + weight
                parent[neighbor] = vertice


