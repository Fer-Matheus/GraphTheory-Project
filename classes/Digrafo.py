from classes.Grafo import Grafo
import heapq, operator
# Tamanho inicial das arestas antes do relaxamento
MAX_TAM = 10000000000000000000000000000000000000000000
class Digrafo(Grafo):
    def __init__(self, caminhoArquivo=str):
        self.listaAdjacencia = {}
        self.LerArquivo(caminhoArquivo)

    def LerArquivo(self, caminhoArquivo):
        with open(caminhoArquivo, "+r") as linha:
            linhas = linha.readlines()

        try:
            for linha in linhas:
                _, verticeA, verticeB, peso = linha.split(" ")
                peso = int(peso)
                if verticeA in self.listaAdjacencia.keys():
                    if "positivo" in self.listaAdjacencia[verticeA].keys():
                        self.listaAdjacencia[verticeA]["positivo"].append(
                            (verticeB, peso))
                    else:
                        self.listaAdjacencia[verticeA].update(
                            {"positivo": [(verticeB, peso)]})
                else:
                    self.listaAdjacencia.update(
                        {verticeA: {"positivo": [(verticeB, peso)]}})
                if verticeB in self.listaAdjacencia.keys():
                    if "negativo" in self.listaAdjacencia[verticeB].keys():
                        self.listaAdjacencia[verticeB]["negativo"].append(
                            (verticeA, peso))
                    else:
                        self.listaAdjacencia[verticeB].update(
                            {"negativo": [(verticeA, peso)]})
                else:
                    self.listaAdjacencia.update(
                        {verticeB: {"negativo": [(verticeA, peso)]}})
        except:
            pass

    def MostrarGrafo(self):
        for vertice in self.listaAdjacencia.keys():
            p, n = self.vizinho(vertice)
            print(
                f'Vertice({vertice}):\n"positivos" : {p} || "negativos" : {n}')

    def vizinho(self, vertice):
        positivos, negativos = set(), set()

        for p in self.listaAdjacencia[vertice]["positivo"]:
            positivos.add(p)
        for n in self.listaAdjacencia[vertice]["negativo"]:
            negativos.add(n)
        return positivos, negativos

    def d(self, vertice):
        vizinhosPositivos, vizinhosNegativos = self.vizinho(vertice)
        return len(vizinhosPositivos), len(vizinhosNegativos)
    
    def minD(self):
        return min([(self.d(vert))[0] for vert in self.listaAdjacencia.keys()]),min([(self.d(vert))[1] for vert in self.listaAdjacencia.keys()])
    
    def maxD(self):
        return max([(self.d(vert))[0] for vert in self.listaAdjacencia.keys()]),max([(self.d(vert))[1] for vert in self.listaAdjacencia.keys()])
    
    # Algoritmo BFS
    def bfs(self, vertice):
        # Temos a inicialização das variaveis de controle da distancia e do verice antecessor
        distancia, antecessor = 0, None

        # inicializamos também dois dicionarios que vão armazenar as distâncias e antecessores de cada vertice
        d, antecessores = {}, {}

        # Visitado será usado para verificar os vertices que já foram iterados, bem como Q é a lista daqueles que ainda serão visitados
        visitado, Q = set(), []

        # Inicializamos pelo vertice escolhido pelo usuário
        d[vertice] = 0
        antecessores[vertice] = None
        Q.append(vertice)

        # Enquanto a fila de vertices a serem visitados não for vazia
        while Q:
            vert = Q.pop(0)

            # Verificamos se o vertice já foi visitado, caso verdade ele será ignorado e passa pro próximo
            if vert in visitado:
                continue

            # Caso não, ele é adicionado a lista de visitados, e a distancia e o antecessor são atualizados
            visitado.add(vert)
            distancia += 1
            antecessor = vert

            # Para cada vizinho do vertice em questão, é atribuido a distância que ele está e que seu antecessor é o vertice em questão
            vizinho = self.vizinho(vert)
            for i, _ in vizinho[0]:
                if i in visitado or i in Q:
                    continue
                d[i] = distancia
                antecessores[i] = antecessor
                Q.append(i)

        return d, antecessores

    # Algoritmo de busca em profundidade (DFS) para grafos
    def dfs(self, vertice):
        # Conjunto para os nós visitados, variavel de tempo e antecessor
        visitado, temp, antecessor = set(), 0, None

        # Dicionários e lista auxiliares
        tempoInicial, tempoFinal, antecessores, Q = {}, {}, {}, []

        # Iniciando a busca com o vértice fornecido
        Q.append(vertice)

        # Enquanto a lista Q não estiver vazia
        while Q:
            vert = Q.pop(0)

            # Se o vértice ainda não foi visitado
            if vert not in visitado:

                # Marca o vértice como visitado e marca o tempo inicial e seu antecessor
                visitado.add(vert)
                temp += 1
                tempoInicial[vert] = temp
                antecessores[vert] = antecessor
                antecessor = vert

                # Obtemos os vizinhos do vértice para inclui-los na lista Q
                vizinhos = self.vizinho(vert)
                for i, _ in vizinhos[0]:

                    # Se o vizinho ainda não foi visitado nem está na lista Q
                    if i not in visitado and i not in Q:
                        Q.append(i)

        # Por fim, marcamos os tempos finais de acesso dos vertices visitados na ordem reversa de entrada
        visitado = sorted(visitado, reverse=True)
        for vert in visitado:
            temp += 1
            tempoFinal[vert] = temp
    
        return tempoInicial, tempoFinal, antecessores

    def BellmanFord(self, vertice):
        # Inicialização dos dicionários para armazenar as distâncias e predecessores
        d, antecessor = {}, {}

        # Define a distância inicial como infinito para todos os vértices
        [d.update({vertice: MAX_TAM})
         for vertice in self.listaAdjacencia.keys()]

        # Define o antecessor inicial como nulo para todos os vértices
        [antecessor.update({vertice: None})
         for vertice in self.listaAdjacencia.keys()]

        # Define a distância do vértice de origem como 0 e seu antecessor como nulo
        d[vertice] = 0
        antecessor[vertice] = None

        while True:
            # Chama a função relaxaBF para atualizar as distâncias
            if not self.relaxaBF(d, antecessor, vertice):
                break

        # Por fim, verificamos se contém ciclos negativos dentro do grafo, mas é apenas como demostração já que o professor deixou claro que essa base não tem ciclos negativos
        for vertice in self.listaAdjacencia.keys():
            vizinhos = self.vizinho(vertice)
            for vizinho, peso in vizinhos[0]:
                # Verifica se há um ciclo negativo no grafo
                if d[vizinho] > d[vertice] + peso:
                    return None, None, "Detectado ciclo negativo"

        # Devolvemos as distâncias, antecessores e o erro como nulo
        return d, antecessor, None

    # Função auxiliar de relaxamento das arestas
    def relaxaBF(self, d, antecessor, raiz):
        # Variável para verificar se houve alteração nas distâncias, foi um meio pensado para evitar iterações desnecessárias
        verificaMudanca = False

        # Começamos relando as arestas dos vizinhos da raiz
        vizinhos = self.vizinho(raiz)
        for vizinho, peso in vizinhos[0]:
            if d[vizinho] > d[raiz] + peso:
                # Atualiza a distância e o antecessor do vizinho se encontrar um caminho mais curto
                d[vizinho] = d[raiz] + peso
                antecessor[vizinho] = raiz

        for vertice in self.listaAdjacencia.keys():
            vizinhos = self.vizinho(vertice)
            for vizinho, peso in vizinhos[0]:
                if d[vizinho] > d[vertice] + peso:
                    # Atualiza a distância e o antecessor do vizinho se encontrar um caminho mais curto
                    d[vizinho] = d[vertice] + peso
                    antecessor[vizinho] = vertice
                    verificaMudanca = True

        return verificaMudanca

    # Algoritmo Dijkstra
    def Dijkstra(self, vertice):

        # Dicionários e listas auxiliares
        d, antecessor, Q, visitado = {}, {}, [], set()

        # Definindo peso e antecessor padrão para todos
        [d.update({vert: MAX_TAM})for vert in self.listaAdjacencia.keys()]
        [antecessor.update({vert: None})
         for vert in self.listaAdjacencia.keys()]

        # Iniciando pelo vértice escolhido pelo usuário
        d[vertice] = 0

        # Aqui usamos um lista de prioridade
        heapq.heappush(Q, vertice)
        """
            vert = A
            A : (C,B)
            Q = B, B
            visitado = C, A
        """

        # Enquanto a lista Q não estiver vazia
        while Q:
            vert = heapq.heappop(Q)  # B

            # Se o vértice já foi visitado, continua para o próximo vértice
            if vert in visitado:
                continue
            visitado.add(vert)

            # Nesse ponto, atualizamos as distâncias dos vizinhos do vértice atual
            self.relaxaDijkstra(d, antecessor, vert)
            vizinhos = self.vizinho(vert)
            for vizinho, _ in vizinhos[0]:
                # Aqueles que já foram visitados, ou ja se encontram na lista de espera, são ignorados
                if vizinho in visitado or vizinho in Q:
                    continue
                heapq.heappush(Q, vizinho)

        # Retorna as distâncias e os antecessores
        return d, antecessor

    def relaxaDijkstra(self, d, antecessor, vertice):

        # Obtém os vizinhos do vértice atual
        vizinhos = self.vizinho(vertice)
        for vizinho, peso in vizinhos[0]:
            # Se encontrar um caminho mais curto para o vizinho, atualizamos sua distância e antecessor
            if d[vizinho] > d[vertice] + peso:
                d[vizinho] = d[vertice] + peso
                antecessor[vizinho] = vertice

    def EncontrarCaminho(self, valor, T):
        # Conjunto de vértices testados e lista para armazenar o caminho
        testados, caminho = set(), []

        for vertice in self.listaAdjacencia.keys():

            # Se o vértice ainda não foi testado, o adicionamos ao caminho
            if vertice not in testados:

                # Marca o vértice como testado
                testados.add(vertice)

                # Obtém o pai do vértice usando a árvore T, gerada usando um dos algoritmos
                pai = T[vertice]

                # Enquanto houver um pai, o adicionamos a lista e atualizamos o pai
                while pai != None:
                    caminho.append(pai)
                    pai = T[pai]

                # Ao chegarmos a raiz, se o tamanho do caminho satisfizer a condição, retornamos o caminho.
                if len(caminho) >= valor:
                    return caminho

                # Do contrário, o caminho é limpo e reiniciado
                else:
                    caminho.clear()
                    continue

        # Caso não haja um caminho com o valor requisitado
        return None
    
    # Algoritmo 
    def BuscarCiclos(self, valor,T):

        ciclos = self.EncontrarCaminho(valor, T)
        
        if ciclos == None:
            return f"Não há ciclos de tamanho >= 5"
        else:
            ciclosReverso = ciclos.copy()
            ciclosReverso.reverse()
            for vertice in ciclos:
                vizinhos = self.vizinho(vertice)
                for vizinho,_ in vizinhos[0]:
                    if ciclosReverso[0] == vizinho:
                        index = ciclos.index(vertice)
                        if index >= 5:
                            ciclo = ciclosReverso[0:index]
                            ciclo.append(ciclosReverso[0])
                            return ciclo
            return f"Não há ciclos de tamanho >= 5"
        
    def MaisDistante(self, vertice):
        d, _ = self.Dijkstra(vertice)
        maior = max(d.items(), key=operator.itemgetter(1))
        
        return maior
            
