def print_solution(caminho):
    
    for i in range(len(caminho)):
        print(caminho[i], end="\n")


def caminha_labirinto(lab,x,y,sx,sy,solucao):

    if x == sx and y == sy:
        solucao[x][y] = "S"
        print_solution(solucao)
        return True

    elif ( (0 <= y < len(lab)) and (0 <= x < len(lab))):

        if ((lab[x][y] == " ") and (solucao[x][y] == " ")):
            solucao[x][y] = "*"

            if (caminha_labirinto(lab, x, y+1, sx, sy, solucao)): # percorrendo labirinto para direita
                return True

            elif(caminha_labirinto(lab, x+1, y, sx, sy, solucao)): # percorrendo labirinto para cima
                return True

            elif(caminha_labirinto(lab, x, y-1, sx, sy, solucao)): # percorrendo labirinto para esquerda
                return True

            elif(caminha_labirinto(lab, x-1, y, sx, sy, solucao)): # percorrendo labirinto para baixo
                return True

            else:
                solucao[x][y] = " "
                
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

caminha_labirinto(lab, 0, 0, 4, 4, caminho_saida)