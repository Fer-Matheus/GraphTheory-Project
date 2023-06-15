from classes.Grafo import Grafo
# Obtendo o caminho do db
caminhoArquivo, nomeArquivo = ("db/USA-road-d.NY.gr.txt",
                      "USA-road-d.NY.gr") if True else ("db/Teste.txt", "Teste")

grafo = Grafo((caminhoArquivo))

while True:
    vertice = input("Choose one vertice: ")
    vertice = vertice.upper() if "Teste" in caminhoArquivo else '12'
    if grafo.verificaVertice(vertice):
        print('\n > Grafo attributes')
        print(f'G.n(): {grafo.n()}')
        print(f'G.m(): {grafo.m()}')
        print(f'G.vizinho({vertice}): {grafo.vizinho(vertice)}')
        print(f'G.d({vertice}): {grafo.d(vertice)}')
        print(f'G.minD(): {grafo.minD()}')
        print(f'G.maxD(): {grafo.maxD()}')

        print('\n')
        print("#"*100)
        print('\n')

        d, antecessores = grafo.bfs(vertice)
        print(
            f'\nBFS Algorithm for the vertice({vertice}): \nDistance:{d}\n\nAntecessores:{antecessores}')

        tempoInicial, tempoFinal, antecessores = grafo.dfs(vertice)

        print(f'\n\nDFS Algorithm for the vertice({vertice}):')
        print(f'tempoInicial: \n{tempoInicial}')
        print(f'tempoFinal: \n{tempoFinal}')
        print(f'antecessores: \n{antecessores}')

        d, antecessores, err = grafo.BellmanFord(vertice)
        if err != None:
            print(err)
        else:
            print(f"BellmanFord Algorithm for the vertice: {vertice}")
            print(f'\nDistance:\n{d}\nantecessores:\n{antecessores}')
        print()

        d, antecessores= grafo.Dijkstra(vertice)
        # print(f"Dijkstra Algorithm for the vertice: {vertice}")
        # print(f'\nDistance:\n{d}\nantecessores:\n{antecessores}')
        valor = int(input("Digite um valor: \n"))
        caminho = grafo.EncontrarCaminho(valor, antecessores)
        
        print(caminho)
        break
    else:
        print(f"The vertice: {vertice} isn't present on this Grafo!")
    
