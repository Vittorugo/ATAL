def caminha_labirinto(lab,x,y,sx,sy,solucao):

    if x == sx and y == sy:
        solucao[x][y] = "*"
        return True

    else:

        if ((lab[x][y] == 0) and (solucao[x][y] == 0)):
            solucao[x][y] = "*"

            if (caminha_labirinto(lab, x, y+1, sx, sy, solucao)):
                return True

            elif(caminha_labirinto(lab, x+1, y, sx, sy, solucao)):
                return True

            elif(caminha_labirinto(lab, x, y-1, sx, sy, solucao)):
                return True

            elif(caminha_labirinto(lab, x-1, y, sx, sy, solucao)):
                return True

            else:
                solucao[x][y] = 0

        else:
            return False

lab = [[0,0,0,0,1],
       [1,1,0,0,1],
       [0,1,0,0,0],
       [0,0,0,1,1],
       [1,1,0,0,0]]


solucao = [[0,0,0,0,1],
           [1,1,0,0,1],
           [0,1,0,0,0],
           [0,0,0,1,1],
           [1,1,0,0,0]]

caminha_labirinto(lab,0,0,4,4,solucao)