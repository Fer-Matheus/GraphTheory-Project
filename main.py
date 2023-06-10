
# Obtendo o caminho do db
file_path = "db\\USA-road-d.NY.gr.txt"

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


