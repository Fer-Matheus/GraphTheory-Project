import heapq

MAX_TAM = 10000000000000000000000000000000000000000000
class Grafo:
    def __init__(self, caminhoArquivo=str):
        self.listaAdjacencia = {}
        self.LerArquivo(caminhoArquivo)

    def verificaVertice(self, vertice):
        return vertice in self.listaAdjacencia.keys()

    def LerArquivo(self, caminhoArquivo):
        # Executando a leitura do db e armazenando em linhas
        with open(caminhoArquivo, "+r") as linha:
            linhas = linha.readlines()

        # Tratando a lista linhas para preencher de forma correta os vertices e arestas
        for linha in linhas:

            _, verticeA, verticeB, peso = linha.split(" ")
            peso = int(peso)
            if verticeA in self.listaAdjacencia.keys():
                self.listaAdjacencia[verticeA].append((verticeB, peso))
            else:
                self.listaAdjacencia.update({verticeA: [(verticeB, peso)]})
            if verticeB in self.listaAdjacencia.keys():
                self.listaAdjacencia[verticeB].append((verticeA, peso))
            else:
                self.listaAdjacencia.update({verticeB: [(verticeA, peso)]})

    def MostrarGrafo(self):
        for vertice in self.listaAdjacencia.keys():
            print(f"{vertice}: {self.vizinho(vertice)}")

    def EscrevelistaAdjacencia(self, nomeArquivo):
        with open(f"db/{nomeArquivo}_listaAdjacencia.txt", "+w") as arquivo:
            for vertice in self.listaAdjacencia.keys():
                arquivo.write(f"{vertice}: {self.vizinho(vertice)}\n")

    def n(self):
        return len(self.listaAdjacencia.keys())

    def m(self):
        arestas = set()
        for aresta in self.listaAdjacencia.values():
            for item in aresta:
                arestas.add(item)
        return len(arestas)

    def vizinho(self, vertice):
        vizinho = set()
        for i in self.listaAdjacencia[vertice]:
            vizinho.add(i)
        return vizinho

    def d(self, vertice):
        return len(self.vizinho(vertice))

    def minD(self):
        return min([self.d(vertice) for vertice in self.listaAdjacencia.keys()])

    def maxD(self):
        return max([self.d(vertice) for vertice in self.listaAdjacencia.keys()])

    def bfs(self, vertice):

        distancia, antecessor = 0, None
        d, antecessores = {}, {}
        visitado, Q = set(), []
        d[vertice] = 0
        antecessores[vertice] = None
        Q.append(vertice)

        while Q:
            vert = Q.pop(0)
            if vert in visitado:
                continue
            visitado.add(vert)
            distancia += 1
            antecessor = vert
            vizinho = self.vizinho(vert)
            for i, _ in vizinho:
                if i in visitado or i in Q:
                    continue
                d[i] = distancia
                antecessores[i] = antecessor
                Q.append(i)
        return d, antecessores

    def dfs(self, vertice):
        visitado, temp, antecessor = set(), 0, None
        tempoInicial, tempoFinal, antecessores, Q = {}, {}, {}, []
        Q.append(vertice)

        while Q:
            vert = Q.pop(0)
            if vert not in visitado:
                visitado.add(vert)
                temp += 1
                tempoInicial[vert] = temp
                antecessores[vert] = antecessor
                vizinhos = self.vizinho(vert)
                antecessor = vert
                for i, _ in vizinhos:
                    if i not in visitado and i not in Q:
                        Q.append(i)
        for vert in visitado:
            tempoFinal[vert] = temp
            temp += 1

        return tempoInicial, tempoFinal, antecessores

    def BellmanFord(self, vertice):
        # inicializando os dicionarios com as distâncias e predecessores
        d, antecessor = {}, {}
        [d.update({vertice: MAX_TAM}) for vertice in self.listaAdjacencia.keys()]
        [antecessor.update({vertice: None})
         for vertice in self.listaAdjacencia.keys()]

        d[vertice] = 0
        antecessor[vertice] = None

        while True:
            if not self.relaxa(d, antecessor, vertice):
                break
        for vertice in self.listaAdjacencia.keys():
            vizinhos = self.vizinho(vertice)
            for vizinho, peso in vizinhos:
                if d[vizinho] > d[vertice] + peso:
                    return None, None, "Negative cicles detect"
        return d, antecessor, None

    def relaxaBF(self, d, antecessor, first):
        verificaMudanca = False        
        vizinhos = self.vizinho(first)
        for vizinho, peso in vizinhos:
            if d[vizinho] > d[first]+peso:
                d[vizinho] = d[first] + peso
                antecessor[vizinho] = first

        for vertice in self.listaAdjacencia.keys():
            vizinhos = self.vizinho(vertice)
            for vizinho, peso in vizinhos:
                if d[vizinho] > d[vertice]+peso:
                    d[vizinho] = d[vertice] + peso
                    antecessor[vizinho] = vertice
                    verificaMudanca = True
        return verificaMudanca
    
    def Dijkstra(self, vertice):
        d, antecessor, Q , visitado = {}, {}, [], set()
        [d.update({vert: MAX_TAM})for vert in self.listaAdjacencia.keys()]
        [antecessor.update({vert: None}) for vert in self.listaAdjacencia.keys()]

        d[vertice] = 0
        heapq.heappush(Q,vertice)
        """
            vert = A
            A : (C,B)
            Q = B, B
            visitado = C, A
        """
        while Q:
            vert = heapq.heappop(Q) # B 
            if vert in visitado:
                continue
            visitado.add(vert) # 
            self.relaxaDijkstra(d,antecessor, vert)
            vizinhos = self.vizinho(vert)
            for vizinho, _ in vizinhos:
                if vizinho in visitado or vizinho in Q:
                    continue
                heapq.heappush(Q,vizinho)
        return d, antecessor


    def relaxaDijkstra(self, d, antecessor,vertice):
        vizinhos = self.vizinho(vertice)
        for vizinho, peso in vizinhos:
            if d[vizinho] > d[vertice] + peso:
                d[vizinho] = d[vertice] + peso
                antecessor[vizinho] = vertice


    def EncontrarCaminho(self, valor, T):
        testados, caminho = set(), []
        for vertice in self.listaAdjacencia.keys():
            if vertice not in testados:
                testados.add(vertice)
                pai = T[vertice]
                while pai != None:
                    caminho.append(pai)
                    pai = T[pai]
                if len(caminho) == valor:
                    return caminho
                else:
                    caminho.clear()
                    continue
