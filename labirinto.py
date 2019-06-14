def print_solution(caminho):

    for i in range(len(caminho)):
        print(caminho[i], end="\n")


def caminha_labirinto(lab, pos_linha, pos_coluna, pos_linha_saida, pos_coluna_saida, solucao):

    if pos_linha == pos_linha_saida and pos_coluna == pos_coluna_saida:
        solucao[pos_linha][pos_coluna] = "S"
        print_solution(solucao)
        return True

    elif ( (0 <= pos_linha < len(lab)) and (0 <= pos_coluna < len(lab))):

        if ((lab[pos_linha][pos_coluna] == " ") and (solucao[pos_linha][pos_coluna] == " ")):
            solucao[pos_linha][pos_coluna] = "*"

            if (caminha_labirinto(lab, pos_linha, pos_coluna+1, pos_linha_saida, pos_coluna_saida, solucao)): # percorrendo labirinto para direita
                return True

            elif(caminha_labirinto(lab, pos_linha+1, pos_coluna, pos_linha_saida, pos_coluna_saida, solucao)): # percorrendo labirinto para cima
                return True

            elif(caminha_labirinto(lab, pos_linha, pos_coluna-1, pos_linha_saida, pos_coluna_saida, solucao)): # percorrendo labirinto para esquerda
                return True

            elif(caminha_labirinto(lab, pos_linha-1, pos_coluna, pos_linha_saida, pos_coluna_saida, solucao)): # percorrendo labirinto para baixo
                return True

            else:
                solucao[pos_linha][pos_coluna] = " "

        else:
            return False

    else:
        return False

lab = [[" "," "," "," ",'#'],
       ["#","#"," "," ","#"],
       [" ",'#'," "," "," "],
       [" "," "," ","#","#"],
       ["#","#"," "," "," "]]

caminho_saida = lab.copy()

entrada = [0,0]
saida   = [4,4]


caminha_labirinto(lab, entrada[0],entrada[1], saida[0], saida[1], caminho_saida)