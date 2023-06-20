from classes.Digrafo import Digrafo
from classes.Grafo import Grafo
#Código que contém todos os casos testes pedidos no trabalho

#Função que imprime no terminal todos casos testes pedidos
def CasosTestes(escolha, caminhoArquivo):
    classe = Grafo(caminhoArquivo) if escolha == 1 else Digrafo(caminhoArquivo)
    #Se for escolhido 1 os casos testes são feitos no grafo, se for 2, serão feitos no digrafo
    tipo = 'G' if escolha == 1 else 'D'

    #A partir do vértice escolhido, imprime todos os casos teste pedidos no trabalho
    vertice = input("Escolha um vértice:\n")
    print("#"*20,end="\n\n")
    print(f'a) O valor de {tipo}.minD(): {classe.minD()}')
    print("#"*20,end="\n\n")
    print(f'b) O valor de {tipo}.maxD(): {classe.maxD()}')
    print("#"*20,end="\n\n")
    _, T = classe.Dijkstra(vertice)
    print(f'c) Um caminho de tamanho 10 ou superior para o vértice ({vertice}):\n{classe.EncontrarCaminho(10,T)}')
    print("#"*20,end="\n\n")
    print(f'd) Um ciclo com uma qtde. de arestas maior ou igual a 5:\n{classe.BuscarCiclos(T)}')
    print("#"*20,end="\n\n")
    print(f'e) O vértice mais distante do vértice 129, e o valor da distância entre eles:\n{classe.MaisDistante(vertice)}')

