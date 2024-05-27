class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_a_estrela = self.vertice.distancia_objetivo + self.custo