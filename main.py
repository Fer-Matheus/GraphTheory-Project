from classes.Grafo import Grafo
from classes.Digrafo import Digrafo
from utils.tools import *
#Código main do projeto

# Obtendo o caminho do BD
caminhoArquivo, nomeArquivo = ("db/USA-road-d.NY.gr.txt",
                               "USA-road-d.NY.gr") if True else ("db/Teste.txt", "Teste")

#Aqui o usuário vai escolher se quer que os casos teste sejam feitos no grafo ou no digrafo
tipo = int(input("Escolha qual o tipo de grafo:\n\t1 - Grafo não orientado\t2 - Digrafo\n"))

#Chamando a função com todos os casos teste pedidos no trabalho
CasosTestes(tipo, caminhoArquivo)
