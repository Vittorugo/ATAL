""" N - Queen """

def print_solution(tab,n):

    for i in range(n):
        print(tab[i], end="\n")

def viavel(tab,linha,col):

    # verificando horizontal e vertical ......

    for check in range(len(tab)):

        if ((tab[linha][col] != tab[linha][check]) or (tab[linha][col] != tab[check][col])):
            return False

    # verificando diagonal principal ...

    for (x,y) in zip(range(linha,-1,-1), range(col, -1, -1)): # parte superior da diagonal principal
        if ( tab[linha][col] != tab[x][y] ):
            return False


    for (x,y) in zip(range(linha,len(tab),1),range(col,len(tab),1)): # parte inferior da diagonal principal
        if ( tab[linha][col] != tab[x][y] ):
            return False

    # verificando diagonal secundaria ...

    for (w,z) in zip(range(linha,-1,-1),range(col, len(tab),1)): # parte superior da diagonal secundária
        if ( tab[linha][col] != tab[w][z] ):
            return False

    for (w,z) in zip(range(linha,len(tab),1), range(col,-1,-1)): # parte inferior da diagonal secundária
        if ( tab[linha][col] != tab[w][z] ):
            return False

    #########################################################3#######

    return True


def backtracking(tab, col, n):

    if( col == n):
        print_solution(tab,n)
        return

    else:

        for i in range(0,n):

            if ( viavel(tab, i, col)):

                tab[i][col] = 1
                R = backtracking(tab, col + 1, n)
                if (R): return R
                tab[i][col] = 0

        return False


tab = [[0]*4]*4

for i in range(len(tab)):
    print(tab[i],end="\n")

print("############### RESULTADO ##########################")

print(backtracking(tab, 0, 4))