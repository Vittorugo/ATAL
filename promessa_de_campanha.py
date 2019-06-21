""" Promessa de campanha """

# Criando o grafo ...

class Grafo():

    def __init__(self):

        self.vertices    = []
        self.arestas     = []
        self.adjacencias = []
        self.pai         = []
        self.cor         = []
        self.distancia   = []



def BFS(G,s):

    G.cor[s]       = "Cinza"    # pintamos s de cinza já que ele é descoberto quando o procedimento começa ...
    G.distancia[s] = 0
    G.pai[s]       = None

    fila=[]
    fila.append(s) # fila que inicializa apenas com o vértice S.

    while( len(fila)!= 0 ):

        u = fila.pop(0) #remove da fila e retorna o elemento do indice dado no parâmetro.

        for v in G.adjacencias[u]:

            if(G.cor[v]== "Branco"):

                G.cor[v]= "Cinza"
                G.distancia[v] = G.distancia[u] + 1 # distancia do vertice s ao vértice u.
                G.pai[v] = u  # predecessor

                fila.append(v)

        G.cor[u] = "Preto"



def prepara_proxima_entrada(grafo):

    grafo.arestas = []     # limpa lista contendo as arestas  do grafo
    grafo.adjacencias = [] # limpa lista de adjacencias descobertos
    grafo.pai = []         # limpa lista de pais descobertos
    grafo.cor = []         # limpa lista de cor descobertos
    grafo.distancia = []   # limpa lista de distancia descobertos


grafo = Grafo()
check = 0
list_temp =[] # lista para armazenar temporariamente os resultados obtidos para as respectivas entradas



while True:

    # 1º linha de entrada: Numero de casos de teste

    t = input().strip()
    t = t.split()

    if (t):
        casos_teste = int(t[0])
        break


while ( check != casos_teste):

    num_estradas_prometidas = 0

    # 2º linha de entrada: Número de pontos principais da cidade.

    N = input().strip()
    N = N.split()

    if (N):

        if (len(N) == 2):

            pontos_principais = int(N[0])
            num_estradas = int(N[1])

            num_estradas_prometidas = pontos_principais - 1 # o número de estradas para interligar todos os pontos sempre será o número de pontos principais menos um.


        else:

            pontos_principais = int(N[0])

            num_estradas_prometidas = pontos_principais - 1 # o número de estradas para interligar todos os pontos sempre será o número de pontos principais menos um.


            # 3º linha de entrada : Número de estradas construídas.

            while (1):

                M = input().strip()
                M = M.split()

                if (M):

                    num_estradas = int(M[0])
                    break

        ####################################   Inicializando Grafo   ##############################################

        for i in range(pontos_principais):
            grafo.vertices.append(i+1)        # Adicionando pontos principais à lista de vertices. Começa do 1.



        # Optei por fazer assim, pois como não consideramos vertice 0 é melhor os indices zeros nas listas serem descartados e Trabalharmos com as lista começando apenas pelo indice 1.
        for i in range(pontos_principais+1):

            if i == 0:
                grafo.cor.append("x")
                grafo.adjacencias.append([None])
                grafo.pai.append(0)
                grafo.distancia.append("x")

            else:
                grafo.cor.append("Branco")
                grafo.adjacencias.append([])
                grafo.pai.append(0)
                grafo.distancia.append(None)


        for i in range(num_estradas):  # criando a matriz para inserir as arestas.
            grafo.arestas.append([])

        #############################################################################################################

        # 4º Entrada = Receber arestas .

        cont = 0

        while ( cont != num_estradas):

            aresta = []

            A = input().strip()
            A = A.split()

            if (A):

                for i in range(2):  # Estou recebendo da entrada as arestas e colocando na lista de aresta do Grafo criado.
                    aresta.append(int(A[i]))
                    grafo.arestas[cont].append(aresta[i])

                cont += 1


        # Inserir vertices adjacentes a lista de adjacencias ...
        for i in range(num_estradas):

            if (grafo.arestas[i][0] in grafo.adjacencias[grafo.arestas[i][1]]):
                pass
            else:
                grafo.adjacencias[grafo.arestas[i][1]].append(grafo.arestas[i][0])

            if (grafo.arestas[i][1] in grafo.adjacencias[grafo.arestas[i][0]]):
                pass
            else:
                grafo.adjacencias[grafo.arestas[i][0]].append(grafo.arestas[i][1])


        for i in range(1,len(grafo.cor)):

            if grafo.cor[i] == "Branco":

                S = i

                BFS(grafo, i)


        soma_pais = 0 # numero total de nós que tem pai
        total     = 0

        for i in range(1,len(grafo.pai)):

            if (grafo.pai[i] != 0 and grafo.pai[i] != None):

                soma_pais += 1


        total = num_estradas_prometidas - soma_pais
        list_temp.append(total)   # armazenando total de estradas que falta para cumprir promessa

        prepara_proxima_entrada(grafo)

        check += 1



for i in range(len(list_temp)):

    if list_temp[i] == 0 :

        print("Caso #%i: a promessa foi cumprida"%(i+1))

    else:
        print("Caso #%i: ainda falta(m)"%(i+1), list_temp[i], "estrada(s)")










