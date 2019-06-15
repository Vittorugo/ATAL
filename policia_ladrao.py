def procura_ladrao(lab, pos_linha, pos_coluna, pos_linha_saida, pos_coluna_saida, solucao):
    
    if pos_linha == pos_linha_saida and pos_coluna == pos_coluna_saida:
        lab[pos_linha][pos_coluna] = "C"
        return True

    else:

        if ( (0 <= pos_linha < len(lab)) and (0 <= pos_coluna < len(lab))):

            if ((lab[pos_linha][pos_coluna] == 0) and (solucao[pos_linha][pos_coluna] == 0)):
                solucao[pos_linha][pos_coluna] = "*"

                if (procura_ladrao(lab, pos_linha, pos_coluna + 1, pos_linha_saida, pos_coluna_saida, solucao)): # percorrendo labirinto para direita
                    return True

                elif(procura_ladrao(lab, pos_linha + 1, pos_coluna, pos_linha_saida, pos_coluna_saida, solucao)): # percorrendo labirinto para cima
                    return True

                elif(procura_ladrao(lab, pos_linha, pos_coluna - 1, pos_linha_saida, pos_coluna_saida, solucao)): # percorrendo labirinto para esquerda
                    return True

                elif(procura_ladrao(lab, pos_linha - 1, pos_coluna, pos_linha_saida, pos_coluna_saida, solucao)): # percorrendo labirinto para baixo
                    return True

                else:
                    solucao[pos_linha][pos_coluna] = 0

            else:
                return False

    return False


###########################################################################################################################################################

num_casos_teste = int(input())

lab = []

for cont in range(num_casos_teste):

    matriz_aux = []
    
    for i in range(5):

        forma_labirinto = input()
        matriz_aux.append([])

        for j in forma_labirinto.split(" "):

            matriz_aux[i].append(int(j))

    lab.append(matriz_aux)


for i in range(num_casos_teste):

    caminho_saida = lab[i].copy()

    if(procura_ladrao(lab[i], 0, 0, 4, 4, caminho_saida)):
        print("Cops")
    else:
        print("Robbes")


