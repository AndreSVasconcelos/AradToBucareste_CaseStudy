from classes.Grafos import GrafoBucareste
from classes.VetoresOrdenados import VetorOrdenado, VetorOrdenadoAEstrela
from classes.Buscas import Gulosa, AEstrela

# Criação do grafo para Bucareste
grafoBucareste = GrafoBucareste()
grafoBucareste.arad.mostra_adjacentes()

# Busca Gulosa
vetor = VetorOrdenado(5)
vetor.insere(grafoBucareste.arad)
vetor.insere(grafoBucareste.craiova)
vetor.insere(grafoBucareste.bucharest)
vetor.insere(grafoBucareste.dobreta)
vetor.insere(grafoBucareste.lugoj)
vetor.imprime()

busca_gulosa = Gulosa(grafoBucareste.bucharest)
busca_gulosa.buscar(grafoBucareste.arad)

# Busca A Estrela
vetorAEstrela = VetorOrdenadoAEstrela(3)
vetorAEstrela.insere(grafoBucareste.arad.adjacentes[0])
vetorAEstrela.insere(grafoBucareste.arad.adjacentes[1])
vetorAEstrela.insere(grafoBucareste.arad.adjacentes[2])
vetorAEstrela.imprime()

busca_a_estrela = AEstrela(grafoBucareste.bucharest)
busca_a_estrela.buscar(grafoBucareste.arad)