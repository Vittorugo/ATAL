""" Desenhando labirintos """


#Criando nossa classe Grafo
class Grafo():

    def __init__(self):

        self.vertices    = [] #lista contendo os vertices do grafo
        self.arestas     = [] #lista contendo as arestas  do grafo
        self.descoberto  = [] #lista de vertices descobertos
        self.adjacencias = [] #lista de  adjacentes

# Busca em profundidade

def DFS_visit(grafo, vertice):

    global contagem
    global vertice_inicio

    if (vertice_inicio != vertice):
        contagem += 1

    grafo.descoberto[vertice] = 1  # quando o vertice é descoberto ele adiciona 1 a lista de descobertos.
    for i in grafo.adjacencias[vertice]:
        if (grafo.descoberto[i] == 0):
            DFS_visit(grafo,i)

def DFS(grafo):

    for vertice in grafo.vertices:
        if( grafo.descoberto[vertice] == 0):
            if (vertice_inicio != vertice):
                DFS_visit(grafo, vertice)


def prepara_proxima_entrada(grafo):

    grafo.vertices   = []  # limpa lista contendo os vertices do grafo
    grafo.arestas    = []  # limpa lista contendo as arestas  do grafo
    grafo.descoberto = []  # limpa lista de vertices descobertos
    grafo.adjacencias= []  # limpa lista de vertices descobertos

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

        contagem = 0

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
                grafo.adjacencias.append([])# alocando nossa lista de adjacencia para colocar os vertices vizinhos conforme indice.

            for i in range(quant_arestas): # criando a matriz para inserir as arestas.
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


            # Alocar a lista de adjacencia ....

            for i in range(quant_arestas):

                if ( grafo.arestas[i][0] in grafo.adjacencias[grafo.arestas[i][1]]):
                    pass
                else:
                    grafo.adjacencias[grafo.arestas[i][1]].append(grafo.arestas[i][0])

                if ( grafo.arestas[i][1] in grafo.adjacencias[grafo.arestas[i][0]]):
                    pass
                else:
                    grafo.adjacencias[grafo.arestas[i][0]].append(grafo.arestas[i][1])


            # podem existir nós desconexos no grafo tempo que marcalos pois eles não seram alcançados pela busca em profundidade.

            for i in range(quant_vertices):

                if ( len(grafo.adjacencias[i]) == 0):
                    grafo.descoberto[i] = "None"

            #chamando a busca em pronfundidade

            DFS(grafo)
            list_temp.append(contagem*2) # multiplico por dois pois em um grafo conexo se você quer partir de um ponto visitar todos os vertices e voltar para esse mesmo ponto o tamanho do caminho percorrido é igual a quantidade de vertices visitados vezes 2.

            #print(grafo.descoberto) para vizualizar os nós que foram descobertos. Nós desconexos não são visitados.

            prepara_proxima_entrada(grafo)

            check += 1

for i in range(len(list_temp)):
    print(list_temp[i])