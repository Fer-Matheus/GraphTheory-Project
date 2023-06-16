from classes.Grafo import Grafo
from classes.Digrafo import Digrafo
# Obtendo o caminho do db
caminhoArquivo, nomeArquivo = ("db/USA-road-d.NY.gr.txt",
                               "USA-road-d.NY.gr") if False else ("db/Teste.txt", "Teste")

tipo = int(
    input("Escolha qual o tipo de grafo:\n\t1 - Grafo não orientado\t2 - Digrafo\n"))

if tipo == 1:
    grafo = Grafo((caminhoArquivo))

    while True:
        vertice = input("Choose one vertice: ")
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

            # d, antecessores = grafo.bfs(vertice)
            # print(
            #     f'\nBFS Algorithm for the vertice({vertice}): \nDistance:{d}\n\nAntecessores:{antecessores}')

            tempoInicial, tempoFinal, antecessores = grafo.dfs(vertice)

            # print(f'\n\nDFS Algorithm for the vertice({vertice}):')
            # print(f'tempoInicial: \n{tempoInicial}')
            # print(f'tempoFinal: \n{tempoFinal}')
            # print(f'antecessores: \n{antecessores}')

            # d, antecessores, err = grafo.BellmanFord(vertice)
            # if err != None:
            #     print(err)
            # else:
            #     print(f"BellmanFord Algorithm for the vertice: {vertice}")
            #     print(f'\nDistance:\n{d}\nantecessores:\n{antecessores}')
            # print()

            # d, antecessores = grafo.Dijkstra(vertice)
            # # print(f"Dijkstra Algorithm for the vertice: {vertice}")
            # # print(f'\nDistance:\n{d}\nantecessores:\n{antecessores}')
            valor = int(input("Digite um valor: \n"))
            caminho = grafo.EncontrarCaminho(valor, antecessores)

            print(caminho)
            
            print(
                f"\nCiclo de tamanho >= 5 detectado: {grafo.BuscarCiclos(valor, antecessores)}")
    
            verticeMaisDistante, peso = grafo.MaisDistante(vertice)
    
            print(f"{verticeMaisDistante} é o vértice mais distante do vertice {vertice}, com o peso {peso}")
            break
        else:
            print(f"The vertice: {vertice} isn't present on this Grafo!")
else:
    digrafo = Digrafo(caminhoArquivo)
    # digrafo.MostrarGrafo()

    vertice = input("Choose one vertice: ")

    print(f'D.d({vertice}): {digrafo.d(vertice)}')
    positivo, negativo = digrafo.minD()
    print(
        f'D.minD({vertice}): "positivos" : {positivo}, "negativos" : {negativo}')

    positivo, negativo = digrafo.maxD()
    print(
        f'D.maxD({vertice}): "positivos" : {positivo}, "negativos" : {negativo}')

    # d, antecessores = digrafo.bfs(vertice)
    # antecessoresB = antecessores
    # print(
    #     f'\nBFS Algorithm for the vertice({vertice}): \nDistance:{d}\n\nAntecessores:{antecessores}')

    # tempoInicial, tempoFinal, antecessores = digrafo.dfs(vertice)

    # print(f'\n\nDFS Algorithm for the vertice({vertice}):')
    # print(f'tempoInicial: \n{tempoInicial}')
    # print(f'tempoFinal: \n{tempoFinal}')
    # print(f'antecessores: \n{antecessores}\n')

    # d, antecessores, err = digrafo.BellmanFord(vertice)
    # if err != None:
    #     print(err)
    # else:
    #     print(f"BellmanFord Algorithm for the vertice: {vertice}")
    #     print(f'Distance:\n{d}\nantecessores:\n{antecessores}')
    #     print()

    # d, antecessores = digrafo.Dijkstra(vertice)
    # print(f"Dijkstra Algorithm for the vertice: {vertice}")
    # print(f'Distance:\n{d}\nantecessores:\n{antecessores}')

    # valor = int(input("Digite um valor: \n"))
    # caminho = digrafo.EncontrarCaminho(valor, antecessores)

    # print(caminho)

    # print(
    #     f"\nCiclo de tamanho >= 5 detectado: {digrafo.BuscarCiclos(valor, antecessores)}")
    
    verticeMaisDistante, peso = digrafo.MaisDistante(vertice)
    
    print(f"{verticeMaisDistante} é o vértice mais distante do vertice {vertice}, com o peso {peso}")
    
