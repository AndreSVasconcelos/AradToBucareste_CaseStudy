from classes.Grafos import GrafoCuritiba
from classes.VetoresOrdenados import VetorOrdenado
from classes.Buscas import Gulosa

# Busca Gulosa
# Criação do grafo para Curitiba
grafoGulosa = GrafoCuritiba()

vetor = VetorOrdenado(16)
vetor.insere(grafoGulosa.portoUniao)
vetor.insere(grafoGulosa.curitiba)
vetor.insere(grafoGulosa.pauloFrontin)
vetor.insere(grafoGulosa.canoinhas)
vetor.insere(grafoGulosa.irati)
vetor.insere(grafoGulosa.saoMatheusDoSul)
vetor.insere(grafoGulosa.tresBarras)
vetor.insere(grafoGulosa.palmeira)
vetor.insere(grafoGulosa.contenda)
vetor.insere(grafoGulosa.lapa)
vetor.insere(grafoGulosa.mafra)
vetor.insere(grafoGulosa.campoLargo)
vetor.insere(grafoGulosa.balsaNova)
vetor.insere(grafoGulosa.araucaria)
vetor.insere(grafoGulosa.saoJoseDosPinhais)
vetor.insere(grafoGulosa.tijucasDoSul)
vetor.imprime() 

print('-----------------------------------------')
print('Busca Gulosa')
busca_gulosa = Gulosa(grafoGulosa.curitiba)
busca_gulosa.buscar(grafoGulosa.portoUniao)