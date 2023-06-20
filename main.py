from classes.Grafo import Grafo
from classes.Digrafo import Digrafo
from utils.tools import *

# Obtendo o caminho do db
caminhoArquivo, nomeArquivo = ("db/USA-road-d.NY.gr.txt",
                               "USA-road-d.NY.gr") if True else ("db/Teste.txt", "Teste")

tipo = int(input("Escolha qual o tipo de grafo:\n\t1 - Grafo não orientado\t2 - Digrafo\n"))

CasosTestes(tipo, caminhoArquivo)