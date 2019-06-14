""" N - Queen """

def print_solution(tab,n):

    for i in range(n):
        print(tab[i], end="\n")

def viavel(tab,linha,col):

    # verificando horizontal e vertical ......

    for check in range(len(tab)):

        if ((tab[linha][col] != tab[linha][check]) or (tab[linha][col] != tab[check][col])):
            return False

    ####################################################################################################
    #########################    verificando diagonal principal ... ####################################
    ####################################################################################################

    #################### parte superior da diagonal principal ########################################

    diagonal_principal_superior = 1

    check_linha_anterior = linha
    check_coluna_anterior = col

    while (check_linha_anterior != 0 and check_coluna_anterior != 0):

        if (tab[linha][col] != tab[linha - diagonal_principal_superior][col - diagonal_principal_superior]):
            return False
            #break

        diagonal_principal_superior += 1
        check_linha_anterior -= 1
        check_coluna_anterior -= 1

    #diagonal_principal_superior = 0

    #for (x,y) in zip(range(linha,-1,-1), range(col, -1, -1)): # parte superior da diagonal principal
     #   if ( tab[linha][col] != tab[x][y] ):
      #      return False


    ##################### parte inferior da diagonal principal #######################################

    diagonal_principal_inferior = 1

    check_linha_posterior = linha
    check_coluna_posterior = col

    while (check_linha_posterior != (len(tab) - 1) and check_coluna_posterior != (len(tab) - 1)):

        if (tab[linha][col] != tab[linha + diagonal_principal_inferior][col + diagonal_principal_inferior]):
            return False
            #break

        diagonal_principal_inferior += 1
        check_linha_posterior += 1
        check_coluna_posterior += 1

    #diagonal_principal_inferior = 0

    #for (x,y) in zip(range(linha,len(tab),1),range(col,len(tab),1)): # parte inferior da diagonal principal
     #   if ( tab[linha][col] != tab[x][y] ):
      #      return False

    ####################################################################################################
    #########################    verificando diagonal secundaria ... ###################################
    ####################################################################################################

    #################### parte superior da diagonal secundaria ########################################

    diagonal_secundaria_superior = 1

    check_linha_anterior = linha
    check_coluna_anterior = col

    while (check_linha_anterior != 0 and check_coluna_anterior != (len(tab) - 1)):

        if (tab[linha][col] != tab[linha - diagonal_secundaria_superior][col + diagonal_secundaria_superior]):
            return False

        diagonal_secundaria_superior += 1
        check_linha_anterior -= 1
        check_coluna_anterior += 1


    #for (w,z) in zip(range(linha,-1,-1),range(col, len(tab),1)): # parte superior da diagonal secundária
     #   if ( tab[linha][col] != tab[w][z] ):
      #      return False

    #################### parte inferior da diagonal secundaria ########################################

    diagonal_secundaria_inferior = 1

    check_linha_posterior = linha
    check_coluna_posterior = col

    while (check_linha_posterior != (len(tab) - 1) and check_coluna_posterior != 0):

        if (tab[linha][col] != tab[linha + diagonal_secundaria_inferior][col - diagonal_secundaria_inferior]):
            return False
            #break

        diagonal_secundaria_inferior += 1
        check_linha_posterior += 1
        check_coluna_posterior -= 1

    #for (w,z) in zip(range(linha,len(tab),1), range(col,-1,-1)): # parte inferior da diagonal secundária
     #   if ( tab[linha][col] != tab[w][z] ):
      #      return False

    ####################################################################################################3#

    return True


def backtracking(tab, col, n):

    if( col == n):
        print_solution(tab,n)
        print("AEEE")
        return

    else:

        for i in range(0,n):

            if ( viavel(tab, i, col)):

                tab[i][col] = "Q"
                R = backtracking(tab, col + 1, n)
                if (R): return R
                tab[i][col] = 0

        return False


tab = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(len(tab)):
    print(tab[i],end="\n")

print("############### RESULTADO ##########################")

backtracking(tab, 0, 4)