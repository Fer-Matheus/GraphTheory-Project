from classes.Graph import Graph
# Obtendo o caminho do db
file_path = "db/USA-road-d.NY.gr.txt"

graph = Graph(file_path)

vertice = '5'

print('\n > Graph attributes')
print(f'G.n(): {graph.n()}')
print(f'G.m(): {graph.m()}')
print(f'G.neighbor({vertice}): {graph.neighbor(vertice)}')
print(f'G.d({vertice}): {graph.d(vertice)}')
print(f'G.minD(): {graph.minD()}')
print(f'G.maxD(): {graph.maxD()}')

print('\n')
print("#"*100)
print('\n')

T = graph.bfs(vertice)
print(f'BFS Algorithm: {T}')
print(f'BFS Algorithm size: {len(T)}')
