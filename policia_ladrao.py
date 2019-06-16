def procura_ladrao(lab, pos_linha, pos_coluna, pos_linha_saida, pos_coluna_saida, solucao):
    if pos_linha == pos_linha_saida and pos_coluna == pos_coluna_saida:
        lab[pos_linha][pos_coluna] = "C"
        return True

    else:

        if ((0 <= pos_linha < len(lab)) and (0 <= pos_coluna < len(lab))):

            if ((lab[pos_linha][pos_coluna] == 0) and (solucao[pos_linha][pos_coluna] == 0)):
                solucao[pos_linha][pos_coluna] = "*"

                if (procura_ladrao(lab, pos_linha, pos_coluna + 1, pos_linha_saida, pos_coluna_saida,
                                   solucao)):  # percorrendo labirinto para direita
                    return True

                elif (procura_ladrao(lab, pos_linha + 1, pos_coluna, pos_linha_saida, pos_coluna_saida,
                                     solucao)):  # percorrendo labirinto para cima
                    return True

                elif (procura_ladrao(lab, pos_linha, pos_coluna - 1, pos_linha_saida, pos_coluna_saida,
                                     solucao)):  # percorrendo labirinto para esquerda
                    return True

                elif (procura_ladrao(lab, pos_linha - 1, pos_coluna, pos_linha_saida, pos_coluna_saida,
                                     solucao)):  # percorrendo labirinto para baixo
                    return True

                else:
                    solucao[pos_linha][pos_coluna] = 0

            else:
                return False

    return False


###########################################################################################################################################################

check = 0
lab = []

# dimensao_matriz = int(input())
# posicao_policia= [0,0]
# posicao_ladrao = [4,4]

while (check < 1):

    num_casos_teste = input()
    if num_casos_teste:
        num_casos_teste = int(num_casos_teste)
        check += 1

for cont in range(num_casos_teste):

    matriz_aux = []
    check = 0

    while (check < 5):

        forma_labirinto = input().strip()
        forma_labirinto = forma_labirinto.split()

        if forma_labirinto:
            matriz_aux.append(list(map(int, forma_labirinto)))
            check += 1

    lab.append(matriz_aux)

for i in range(num_casos_teste):

    caminho_saida = lab[i].copy()

    if (procura_ladrao(lab[i], 0, 0, 4, 4, caminho_saida)):
        print("COPS")
    else:
        print("ROBBERS")

