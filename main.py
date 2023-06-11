from classes.Graph import Graph
# Obtendo o caminho do db
file_path = "db/USA-road-d.NY.gr.txt" if False else "db/Teste.txt"

graph = Graph(file_path)

vertice = 'A' if "Teste" in file_path else '5'

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

d, fathers = graph.bfs(vertice)
print(f'\nBFS Algorithm: \nDistance:{d}\n\nFathers:{fathers}')

initTime, endTime, fathers = graph.dfs(vertice)

print(f'\n\nDFS Algorithm:')
print(f'InitTime: {initTime}')
print(f'EndTime: {endTime}')
print(f'Fathers: {fathers}')
