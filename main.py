from classes.Grafos import Grafo
from classes.VetoresOrdenados import VetorOrdenado

grafo = Grafo()
grafo.arad.mostra_adjacentes()

vetor = VetorOrdenado(5)
vetor.insere(grafo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.bucharest)
vetor.insere(grafo.dobreta)
vetor.imprime()

vetor.insere(grafo.lugoj)
vetor.imprime()