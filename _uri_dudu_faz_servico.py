""" dudu faz serviço """

class Grafo():

    def __init__(self):

        self.vertices    = []
        self.arestas     = []
        self.adjacencias = []
        self.cor         = []

# Busca em profundidade

def DFS_visit(grafo, vertice):

    global ciclo
    global  lista_ciclo


    grafo.cor[vertice] = "cinza"  # quando o vertice é descoberto ele adiciona 1 a lista de descobertos.

    for i in grafo.adjacencias[vertice]:

        if lista_ciclo[0] == i and grafo.cor[lista_ciclo[0]] == "cinza":

            lista_ciclo.append(i)
            ciclo = True

        if (grafo.cor[i] == "Branco"):

            DFS_visit(grafo,i)

def DFS(grafo):

    for vertice in grafo.vertices:

        lista_ciclo.append(vertice)

        #if( grafo.cor[vertice] == "Branco"): Para esta questão é desnecessário esta verificação.
        DFS_visit(grafo, vertice)

        grafo.cor[vertice] = "Branco"
        lista_ciclo.clear()


def prepara_proxima_entrada(grafo):

    grafo.vertices   = []  # limpa lista contendo os vertices do grafo
    grafo.arestas    = []  # limpa lista contendo as arestas  do grafo
    grafo.cor = []  # limpa lista de vertices descobertos
    grafo.adjacencias= []  # limpa lista de vertices descobertos




grafo      = Grafo()
list_temp  = []  # armazena temporariamente o resultado das entradas
ciclo      = False
lista_ciclo = [] # lista que auxilia o dfs a encontrar ciclos.


while True:

    t = input().strip()
    t = t.split()

    if (t):

        num_casos_teste = int(t[0])
        break


cont = 0

while (cont != num_casos_teste) :


    # 2º entrada : N : número de documentos /  M : dependências existentes

    entrada = input().strip()
    entrada = entrada.split()

    if (entrada and len(entrada)== 2):

        N = int(entrada[0])
        M = int(entrada[1])



        ####################################   Inicializando Grafo   ##############################################

        for i in range(N):
            grafo.vertices.append(i+1)        # Adicionando os documentos à lista de vertices. Começa do 1.



        # Optei por fazer assim, pois como não consideramos vertice 0 é melhor os indices zeros nas listas serem descartados e Trabalharmos com as lista começando apenas pelo indice 1.
        for i in range(N+1):

            if i == 0:
                grafo.cor.append("x")
                grafo.adjacencias.append([None])

            else:
                grafo.cor.append("Branco")
                grafo.adjacencias.append([])


        for i in range(M):  # criando a matriz para inserir as arestas.
            grafo.arestas.append([])

        ######################################################################################################3333

        cont_1 = 0

        while (cont_1 < M):

            # 3º linha de entrada: Quantidade de arestas do nosso grafo
            aresta = []

            A = input().strip()
            A = A.split()

            if (A):

                for i in range(2):  # Estou recebendo da entrada as arestas e colocando na lista de aresta do Grafo criado.
                    aresta.append(int(A[i]))
                    grafo.arestas[cont_1].append(aresta[i])

                cont_1 += 1
    
        # Alocar a lista de adjacencia. Grafo direcionado ....

        for i in range(M+1):

            if (grafo.arestas[i][1] in grafo.adjacencias[grafo.arestas[i][0]]):
                pass
            else:
                grafo.adjacencias[grafo.arestas[i][0]].append(grafo.arestas[i][1])


        ciclo = False # verificar se tem ciclo.

        DFS(grafo)

        list_temp.append(ciclo)
        prepara_proxima_entrada(grafo)

        cont += 1


for i in range(len(list_temp)):

    if list_temp[i] == True: print("SIM")
    else: print("NAO")




