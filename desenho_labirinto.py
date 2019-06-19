""" Desenhando labirintos """


#Criando nossa classe Grafo
class Grafo():

    def __init__(self):

        self.vertices    = [] #lista contendo os vertices do grafo
        self.arestas     = [] #lista contendo as arestas  do grafo
        self.descoberto  = [] #lista de vertices descobertos
        self.pai         = [] #vertices pai
        self.salto       = [] #lista com saltos

# Busca em profundidade

def DFS_visit(grafo, vertice):

    global tempo

    tempo += 1

    grafo.descoberto[vertice] = tempo
    for i in grafo.arestas[vertice]:
        if (grafo.descoberto[i] == 0):
            DFS_visit(grafo,i)
            grafo.pai[i] = vertice


    tempo += 1
    grafo.salto[vertice] = tempo

def DFS(grafo):

    for vertice in grafo.vertices:
        if( grafo.descoberto[vertice] == 0):
            DFS_visit(grafo, vertice)


def prepara_proxima_entrada(grafo):

    grafo.vertices   = []  # limpa lista contendo os vertices do grafo
    grafo.arestas    = []  # limpa lista contendo as arestas  do grafo
    grafo.descoberto = []  # limpa lista de vertices descobertos
    grafo.pai        = []  # limpa lista vertices pai
    grafo.salto      = []  # limpa lista com saltos


grafo = Grafo()
check = 0
list_temp =[]

while True:

    # 1º linha de entrada: Numero de casos de teste

    t = input().strip()
    t = t.split()

    if (t):
        casos_teste = int(t[0])
        break


while (check != casos_teste):

        tempo = 0

        # 2º linha de entrada: Vertice inicial onde o desenho deve ser iniciado.

        N = input().strip()
        N = N.split()

        if (N):

            vertice_inicio = int(N[0])

        while(1):

            # 3º linha de entrada: Numero de vertices e arestas

            V_A = input().strip()
            V_A = V_A.split()

            if(V_A):

                quant_vertices = int(V_A[0])
                quant_arestas = int(V_A[1])
                break

        for i in range(quant_vertices): # adicionando os vertices da instância Grafo criada.
            grafo.vertices.append(i)
            grafo.descoberto.append(0)  # alocando indices para inserir os vertices descobertos.
            grafo.pai.append(0)         # alocando indices para depois inserir os nós que são pais.

        for i in range(quant_arestas): # criando a matriz de adjacencias para inserir as arestas.
            grafo.arestas.append([])

        cont = 0
        while (cont <  quant_arestas):

            # 4º linha de entrada: Quantidade de arestas do nosso grafo
            aresta = []

            A = input().strip()
            A = A.split()

            if (A):

                for i in range(2):  # Estou recebendo da entrada as arestas e colocando na lista de aresta do Grafo criado.
                    aresta.append(int(A[i]))
                    grafo.arestas[cont].append(aresta[i])

                cont += 1

        DFS(grafo)
        list_temp.append(tempo)
        prepara_proxima_entrada(grafo)

        check += 1

for i in range(len(list_temp)):
    print(list_temp[i])