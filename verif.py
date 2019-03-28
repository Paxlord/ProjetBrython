def ligneColonneIdentique(taille, tableau):

    TotalColonneIdentique = []
    TotalLigneIdentique = []

    for k in range(0, taille-1):

        for i in range(k, taille-1):

            colonneIdentique = True
            ligneIdentique = True

            for j in range(0, taille):

                if tableau[j][k] != tableau[j][i+1]:
                    colonneIdentique = False
                
                if tableau[k][j] != tableau[i+1][j]:
                    ligneIdentique = False

            TotalColonneIdentique.append(colonneIdentique)
            TotalLigneIdentique.append(ligneIdentique)


    for i in range(0, len(TotalColonneIdentique)):
        if(TotalColonneIdentique[i] or TotalLigneIdentique[i]):
            return True

    return False

def memeNombreZeroUn(taille, tableau, colonne):
    
    
    if colonne:
        firstRow = [0,0]
        for i in range(0, taille):
            if tableau[i][0] == 1:
                firstRow[0] += 1
            else:
                firstRow[1] += 1
        
        if(firstRow[0] != firstRow[1]):
            return False
        
        for i in range(0, taille):

            rowToTest= [0,0]

            for j in range(0, taille):
                if tableau[i][j] == 1:
                    rowToTest[0] += 1
                else:
                    rowToTest[1] += 1
            
            if rowToTest[0] != firstRow[0] or rowToTest[1] != firstRow[1]:
                return False
    else:
        firstColumn = [0,0]
        for i in range(0, taille):
            if tableau[0][i] == 1:
                firstColumn[0] += 1
            else:
                firstColumn[1] += 1
        
        if(firstColumn[0] != firstColumn[1]):
            return False
        
        for i in range(0, taille):

            columnToTest = [0,0]

            for j in range(0, taille):
                if tableau[j][i] == 1:
                    columnToTest[0] += 1
                else:
                    columnToTest[1] += 1
            
            if columnToTest[0] != firstColumn[0] or columnToTest[1] != firstColumn[1]:
                return False
    
    return True

def ZeroUnConsecutif(taille, tableau, colonne):

    for i in range(0, taille):
        print(taille)
        for j in range(0, taille - 2):
            if (tableau[i][j] == tableau[i][j+1]) and (tableau[i][j+1] == tableau[i][j+2]):
                return True

    for i in range(0, taille):
        for j in range(0, taille -2):
            if tableau[j][i] == tableau[j+1][i] and tableau[j+1][i] == tableau[j+2][i]:
                return True

    return False

def grillePleine(taille, tableau):

    for i in range(0, taille):
        for j in range(0, taille):
            if(tableau[i][j] == -1):
                return False
    
    return True