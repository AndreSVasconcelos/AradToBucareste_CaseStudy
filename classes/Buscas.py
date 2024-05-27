from classes.VetoresOrdenados import VetorOrdenado, VetorOrdenadoAEstrela

class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False
    
    def buscar(self, atual):
        print('--------------')
        print('Caminho atual: ', atual.rotulo)
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenadoAEstrela(len(atual.adjacentes))

            for adjacente in atual.adjacentes:
                if not adjacente.vertice.visitado:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente)
            
            vetor_ordenado.imprime()
            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].vertice)


class Gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('--------------')
        print('Caminho atual: ', atual.rotulo)
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))

            for adjacente in atual.adjacentes:
                if not adjacente.vertice.visitado:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente.vertice)

            vetor_ordenado.imprime()
            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0])