from classes.Vertices import Vertice
from classes.Adjacentes import Adjacente

class GrafoCuritiba:
    # Cria as cidades como Vertices com a distancia total até o objetivo final(Curitiba)
    portoUniao = Vertice('Porto Uniao', 203)
    curitiba = Vertice('Curitiba', 0)
    pauloFrontin = Vertice('Paulo Frontin', 172)
    canoinhas = Vertice('Canoinhas', 141)
    tresBarras = Vertice('Tres Barras', 131)
    saoMatheusDoSul = Vertice('Sao Matheus Do Sul', 123)
    irati = Vertice('Irati', 139)
    palmeira = Vertice('Palmeira', 59)
    mafra = Vertice('Mafra', 94)
    campoLargo = Vertice('Campo Largo', 27)
    balsaNova = Vertice('Balsa Nova', 41)
    lapa = Vertice('Lapa', 74)
    tijucasDoSul = Vertice('Tijucas Do Sul', 56)
    araucaria = Vertice('Araucaria', 23)
    saoJoseDosPinhais = Vertice('Sao Jose Dos Pinhais', 13)
    contenda = Vertice('Contenda', 39)

    # Cria a relação de adjacencia entre as cidades vizinhas, com a distancia entre uma e outra
    portoUniao.adiciona_adjacente(Adjacente(pauloFrontin, 46))
    portoUniao.adiciona_adjacente(Adjacente(saoMatheusDoSul, 87))
    portoUniao.adiciona_adjacente(Adjacente(canoinhas, 78))

    pauloFrontin.adiciona_adjacente(Adjacente(portoUniao, 46))
    pauloFrontin.adiciona_adjacente(Adjacente(irati, 75))

    canoinhas.adiciona_adjacente(Adjacente(portoUniao, 78))
    canoinhas.adiciona_adjacente(Adjacente(tresBarras, 12))
    canoinhas.adiciona_adjacente(Adjacente(mafra, 66))

    irati.adiciona_adjacente(Adjacente(pauloFrontin, 75))
    irati.adiciona_adjacente(Adjacente(palmeira, 75))
    irati.adiciona_adjacente(Adjacente(saoMatheusDoSul, 57))

    saoMatheusDoSul.adiciona_adjacente(Adjacente(portoUniao, 87))
    saoMatheusDoSul.adiciona_adjacente(Adjacente(palmeira, 77))
    saoMatheusDoSul.adiciona_adjacente(Adjacente(irati, 57))
    saoMatheusDoSul.adiciona_adjacente(Adjacente(tresBarras, 43))
    saoMatheusDoSul.adiciona_adjacente(Adjacente(lapa, 60))

    tresBarras.adiciona_adjacente(Adjacente(canoinhas, 12))
    tresBarras.adiciona_adjacente(Adjacente(saoMatheusDoSul, 43))

    palmeira.adiciona_adjacente(Adjacente(irati, 75))
    palmeira.adiciona_adjacente(Adjacente(saoMatheusDoSul, 77))
    palmeira.adiciona_adjacente(Adjacente(campoLargo, 55))

    contenda.adiciona_adjacente(Adjacente(balsaNova, 19))
    contenda.adiciona_adjacente(Adjacente(lapa, 26))
    contenda.adiciona_adjacente(Adjacente(araucaria, 18))

    lapa.adiciona_adjacente(Adjacente(saoMatheusDoSul, 60))
    lapa.adiciona_adjacente(Adjacente(contenda, 26))
    lapa.adiciona_adjacente(Adjacente(mafra, 57))

    mafra.adiciona_adjacente(Adjacente(canoinhas, 66))
    mafra.adiciona_adjacente(Adjacente(lapa, 57))
    mafra.adiciona_adjacente(Adjacente(tijucasDoSul, 99))
    
    campoLargo.adiciona_adjacente(Adjacente(palmeira, 55))
    campoLargo.adiciona_adjacente(Adjacente(balsaNova, 22))
    campoLargo.adiciona_adjacente(Adjacente(curitiba, 29))

    balsaNova.adiciona_adjacente(Adjacente(contenda, 19))
    balsaNova.adiciona_adjacente(Adjacente(campoLargo, 22))
    balsaNova.adiciona_adjacente(Adjacente(curitiba, 51))

    araucaria.adiciona_adjacente(Adjacente(contenda, 18))
    araucaria.adiciona_adjacente(Adjacente(curitiba, 37))

    saoJoseDosPinhais.adiciona_adjacente(Adjacente(curitiba, 15))
    saoJoseDosPinhais.adiciona_adjacente(Adjacente(tijucasDoSul, 49))

    tijucasDoSul.adiciona_adjacente(Adjacente(mafra, 99))
    tijucasDoSul.adiciona_adjacente(Adjacente(saoJoseDosPinhais, 49))

    curitiba.adiciona_adjacente(Adjacente(balsaNova, 51))
    curitiba.adiciona_adjacente(Adjacente(campoLargo, 29))
    curitiba.adiciona_adjacente(Adjacente(araucaria, 37))
    curitiba.adiciona_adjacente(Adjacente(saoJoseDosPinhais, 15))

class GrafoBucareste:
    # Cria as cidades como Vertices com a distancia total até o objetivo final(Bucareste)
    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)
    
    # Cria a relação de adjacencia entre as cidades vizinhas, com a distancia entre uma e outra
    arad.adiciona_adjacente(Adjacente(zerind, 75))
    arad.adiciona_adjacente(Adjacente(sibiu, 140))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))

    zerind.adiciona_adjacente(Adjacente(arad, 75))
    zerind.adiciona_adjacente(Adjacente(oradea, 71))

    oradea.adiciona_adjacente(Adjacente(zerind, 71))
    oradea.adiciona_adjacente(Adjacente(sibiu, 151))

    sibiu.adiciona_adjacente(Adjacente(oradea, 151))
    sibiu.adiciona_adjacente(Adjacente(arad, 140))
    sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
    sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

    timisoara.adiciona_adjacente(Adjacente(arad, 118))
    timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

    lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
    lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

    mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

    dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
    dobreta.adiciona_adjacente(Adjacente(craiova, 120))

    craiova.adiciona_adjacente(Adjacente(dobreta, 120))
    craiova.adiciona_adjacente(Adjacente(pitesti, 138))
    craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

    rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
    rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
    rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

    fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
    fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

    pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
    pitesti.adiciona_adjacente(Adjacente(craiova, 138))
    pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

    bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
    bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
    bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))