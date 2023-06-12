from classes.Graph import Graph
# Obtendo o caminho do db
filePath, fileName = ("db/USA-road-d.NY.gr.txt",
                      "USA-road-d.NY.gr") if True else ("db/Teste.txt", "Teste")

graph = Graph((filePath))

vertice = 'A' if "Teste" in filePath else '12'

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

