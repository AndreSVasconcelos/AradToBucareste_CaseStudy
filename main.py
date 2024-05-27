from classes.Grafos import Grafo
from classes.VetoresOrdenados import VetorOrdenado, VetorOrdenadoAEstrela
from classes.Buscas import Gulosa, AEstrela

# Criação do grafo
grafo = Grafo()
grafo.arad.mostra_adjacentes()

# Busca Gulosa
""" vetor = VetorOrdenado(5)
vetor.insere(grafo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.bucharest)
vetor.insere(grafo.dobreta)
vetor.insere(grafo.lugoj)
vetor.imprime()

busca_gulosa = Gulosa(grafo.bucharest)
busca_gulosa.buscar(grafo.arad) """

# Busca A Estrela
vetorAEstrela = VetorOrdenadoAEstrela(3)
vetorAEstrela.insere(grafo.arad.adjacentes[0])
vetorAEstrela.insere(grafo.arad.adjacentes[1])
vetorAEstrela.insere(grafo.arad.adjacentes[2])
vetorAEstrela.imprime()

busca_a_estrela = AEstrela(grafo.bucharest)
busca_a_estrela.buscar(grafo.arad)