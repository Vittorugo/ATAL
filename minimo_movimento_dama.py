def minimo_movimento_rainha(tab, xi, yi, xf, yf):
    
    mov = 0
    # se o valor de entrada for igual ao de destino a solução é zero

    if (xi == xf and yi == yf):
        return mov

    else:

        #verificar linha e coluna na posição atual

        for check in range(len(tab)):

            if (tab[check][yi] == 1 or tab[xi][check] == 1) and ( (check == xf and yi == yf) or (xi == xf and check == yf) ) :
                mov += 1


        #verificar diagonais

        for i,j in zip( range(xi,-1,-1), range(yi,-1,-1)): # principal superior

            if ( (tab[i][j] == 1) and ( i == xf and j == yf)):

                mov += 1

        for i,j in zip( range(xi, len(tab),1), range(yi, len(tab), 1)): # principal inferior

            if ( tab[i][j] == 1 and ( i == xf and j == yf) ):

                mov += 1

        for i,j in zip( range(xi, -1, -1), range(yi, len(tab), 1)): # secundária superior

            if tab[i][j] == 1 and ( i == xf and j == yf):

                mov += 1

        for i,j in zip( range(xi, len(tab),1), range(yi, -1,-1)):

            if tab[i][j] == 1 and ( i == xf and j == yf):

                mov += 1

        ########################################################

        # Se chegar até esse ponto e não for encontrado o caminho de destino a rainha poderá chegar com dois movimentos no          mínimo. Tendo em vista que ela alcança qualquer lugar do tabuleiro através das diagonais formando 1 mov + o necessário para alcançar a casa de destino. Formando 2 movimentos.

        if (mov == 0):

            mov += 2


    return mov


########################################################################################
      # 0 1 2 3 4 5 6 7
tab = [[0,0,0,0,0,0,0,0], # 0
       [0,0,0,0,0,0,0,0], # 1
       [0,0,0,0,0,0,0,0], # 2
       [0,0,0,0,0,0,0,0], # 3
       [0,0,0,0,0,0,0,0], # 4
       [0,0,0,0,0,0,0,0], # 5
       [0,0,0,0,0,0,0,0], # 6
       [0,0,0,0,0,0,0,0]] # 7

lista_resultado = []

xi = 1
yi = 1

xf = 1
yf = 1


lista_de_entradas = []

while ( not( xi == 0 and yi == 0 and xf == 0 and yf == 0)):

    tab_temp = tab # tabela temporária que vai receber as coordenadas para cada entrada do laço

    coordenadas = input() # recebendo entrada

    coordenadas = coordenadas.split(" ")

    if (coordenadas[0] == "0" and coordenadas[1] == "0" and coordenadas[2] == "0" and coordenadas[3] == "0"): # condição de saída do laço dada na entrada " 0 0 0 0 "
        break

    else:

        lista_de_entradas  = list(map(int, coordenadas))  # convertendo a string de entrada em uma lista de inteiros.

        # separando as coordenadas adicionada na lista anteriormente 

        xi = lista_de_entradas[0] 
        yi = lista_de_entradas[1]
        xf = lista_de_entradas[2]
        yf = lista_de_entradas[3]

        # adicionando os pontos de origem e destino na tabela temporária

        tab_temp[xi][yi] = 1
        tab_temp[xf][yf] = 1

        #chamando a função e adicionando o resultado de cada entrada em uma lista
        lista_resultado.append( minimo_movimento_rainha(tab_temp, xi, yi, xf, yf))


for i in range(len(lista_resultado)):

    # exibindo o resultado para cada entrada
    print(lista_resultado[i])
