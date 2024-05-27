from classes.Grafos import GrafoCuritiba
from classes.VetoresOrdenados import VetorOrdenado, VetorOrdenadoAEstrela
from classes.Buscas import Gulosa, AEstrela

# Busca A Estrela
grafoAEstrela = GrafoCuritiba()

vetorAEstrela = VetorOrdenadoAEstrela(3)
for adjacente in grafoAEstrela.portoUniao.adjacentes:
    vetorAEstrela.insere(adjacente)
    
vetorAEstrela.imprime()

print('-----------------------------------------')
print('Busca A*')
busca_a_estrela = AEstrela(grafoAEstrela.curitiba)
busca_a_estrela.buscar(grafoAEstrela.portoUniao)