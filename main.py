from classes.Graph import Graph
# Obtendo o caminho do db
filePath, fileName = ("db/USA-road-d.NY.gr.txt",
                      "USA-road-d.NY.gr") if False else ("db/Teste.txt", "Teste")

graph = Graph((filePath))

while True:
    vertice = input("Choose one vertice: ")
    vertice = vertice.upper() if "Teste" in filePath else '12'
    if graph.verifyVertice(vertice):
        print('\n > Graph attributes')
        print(f'G.n(): {graph.n()}')
        print(f'G.m(): {graph.m()}')
        print(f'G.neighbor({vertice}): {graph.neighbor(vertice)}')
        print(f'G.d({vertice}): {graph.d(vertice)}')
        print(f'G.minD(): {graph.minD()}')
        print(f'G.maxD(): {graph.maxD()}')

        # print('\n')
        # print("#"*100)
        # print('\n')

        # d, fathers = graph.bfs(vertice)
        # print(
        #     f'\nBFS Algorithm for the vertice({vertice}): \nDistance:{d}\n\nFathers:{fathers}')

        # initTime, endTime, fathers = graph.dfs(vertice)

        # print(f'\n\nDFS Algorithm for the vertice({vertice}):')
        # print(f'InitTime: \n{initTime}')
        # print(f'EndTime: \n{endTime}')
        # print(f'Fathers: \n{fathers}')
        d, father, err = graph.BellmanFord(vertice)
        if err != None:
            print(err)
        else:
            print(f"BellmanFord Algorithm for the vertice: {vertice}")
            print(f'\nDistance:\n{d}\nFather:\n{father}')
        print()
        break
    else:
        print(f"The vertice: {vertice} isn't present on this graph!")
    
