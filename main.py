from classes.Graph import Graph
# Obtendo o caminho do db
file_path = "db/USA-road-d.NY.gr.txt"

adjacencyList = {}

# Executando a leitura do db e armazenando em lines
with open(file_path, "+r") as line:
    lines = line.readlines()

# Tratando a lista lines para preencher de forma correta os vertices e arestas
for line in lines:

    _, verticeA, verticeB, weight = line.split(" ")
    if verticeA in adjacencyList.keys():
        adjacencyList[verticeA].append((verticeB, weight))
    else:
        adjacencyList.update({verticeA : [(verticeB,weight)]})

graph = Graph(adjacencyList)

vertice = '1'

print('Graph attributes')
print(f'G.n(): {graph.n()}')
print(f'G.m(): {graph.m()}')
print(f'G.neighbor({vertice}): {graph.neighbor(vertice)}')
print(f'G.d({vertice}): {graph.d(vertice)}')
print(f'G.minD(): {graph.minD()}')
print(f'G.maxD(): {graph.maxD()}')
print("#"*100)
T = graph.bfs(vertice)
print(f'BFS Algorithm: {T}')
print(f'BFS Algorithm size: {len(T)}')