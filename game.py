from browser import document, timer, ajax
from browser.html import TABLE, TD, TR, CANVAS, IMG
import math
from verif import *

tailleTableau = 4
tailleCase = 64
casePadding = 5
tableau = []
clickableTableau = []
currentTableauString = ""
correctedTableau = []
canvas = CANVAS(width = 64, height = 64)

sizeX = 0
sizeY = 0

idTimer = 0

image1 = IMG(src="TileOne.png")
image0 = IMG(src="TileZero.png")
imageE = IMG(src="EmtyTile.png")

def getIndexByMousePos(mouseX, mouseY):
    yOrigin = canvas.abs_top
    xOrigin = canvas.abs_left

    return { 'x': math.floor((mouseX - xOrigin)/(tailleCase+casePadding)), 'y': math.floor((mouseY - yOrigin)/(tailleCase+casePadding))}

def cellClickEvent(ev):
    coordClick = getIndexByMousePos(ev.x, ev.y)
    
    x = coordClick['y']
    y = coordClick['x']

    
    if(clickableTableau[x][y] == True):
        
        if tableau[x][y] == -1:
            tableau[x][y] = 1

        elif tableau[x][y] == 1:
            tableau[x][y] = 0

        elif tableau[x][y] == 0:
            tableau[x][y] = -1

    
    
def verifRoutine(tableau, taille):

    ligneIdentique = ligneColonneIdentique(taille, tableau)
    nombreZeroUn = memeNombreZeroUn(taille, tableau, True) and memeNombreZeroUn(taille, tableau, False)
    zeroUnCons = ZeroUnConsecutif(taille, tableau, True) and ZeroUnConsecutif(taille ,tableau, False)
    grillepleine = grillePleine(taille, tableau)

    print(tableau)
    print(ligneIdentique, nombreZeroUn, zeroUnCons)

    if not ligneIdentique and nombreZeroUn and not zeroUnCons and grillepleine:
        return True
    else:
        return False

def verifEvent(ev):

    if verifRoutine(tableau, tailleTableau):
        document["victoire"].text = ""
        document["victoire"].style.color = "green"
        document["victoire"] <= "Vous avez gagné !"
    else:
        document["victoire"].text = ""
        document["victoire"].style.color = "red"
        document["victoire"] <= "La grille n'est pas correcte ! réessayez !"




def initPlateau():
    plateau = []

    global clickableTableau
    clickableTableau = []

    for i in range(0, tailleTableau):

        ligne = []
        clickableLigne = []

        for j in range(0, tailleTableau):
            ligne.append(-1)
            clickableLigne.append(True)

        plateau.append(ligne)
        clickableTableau.append(clickableLigne)

    return plateau

def afficherPlateauTexte(id, plateau):
    document[id].text = ""
    table = TABLE("", id="tableau")
    for i in range(0, tailleTableau):
        row = TR()
        for j in range(0, tailleTableau):

            if plateau[i][j] == -1:
                cell = TD(" ")
            else:
                cell = TD(plateau[i][j])
            cell.bind("click", cellClickEvent)
            row <= cell

        table <= row
    document[id] <= table

def afficherPlateauCanvas(plateau, canvas):
    ctx = canvas.getContext("2d")
    for i in range(0, tailleTableau):
        for j in range(0, tailleTableau):
            if plateau[j][i] == -1:
                ctx.drawImage(imageE, i*tailleCase + i*casePadding, j*tailleCase + j*casePadding ,tailleCase,tailleCase)
            elif plateau[j][i] == 1:
                ctx.drawImage(image1, i*tailleCase + i*casePadding, j*tailleCase + j*casePadding ,tailleCase,tailleCase)
            else:
                ctx.drawImage(image0, i*tailleCase + i*casePadding, j*tailleCase + j*casePadding ,tailleCase,tailleCase)

def clearCanvas(canvas):
    ctx = canvas.getContext("2d")
    ctx.clearRect(0,0,canvas.width, canvas.height)

def render():
    clearCanvas(canvas)   
    afficherPlateauCanvas(tableau, canvas)

def gameLoop():
    render()

def convertStringToTab(string):

    global clickableTableau
    global tailleTableau

    array = string.split(" ")
    finalArray = []

    taille = tailleTableau


    for i in range(0, taille):

        ligne = []

        for j in range(0, taille):

            if array[i][j] == '/':
                ligne.append(-1)
            else:
                ligne.append(int(array[i][j]))
                clickableTableau[i][j] = False


        finalArray.append(ligne)

    return finalArray


def startGame(string):

    global tableau
    global canvas
    global idTimer

    document["zone"].text = ""

    tableau = initPlateau()
    
    if len(string) != 0:
        tableau = convertStringToTab(string)

    canvas = CANVAS(width = tailleTableau*64 + tailleTableau*5, height = tailleTableau*64 + tailleTableau*5)
    canvas.bind("click", cellClickEvent)

    document["zone"] <= canvas
    idTimer = timer.set_interval(gameLoop, 16)


def generateEvent():

    timer.clear_interval(idTimer)

    select = document["select-size"]
    tailleChoisie = select.options[select.selectedIndex].value

    global tailleTableau
    tailleTableau = int(tailleChoisie)

    ajaxEvent()



def reqComplete(req):
    startGame(req.text)

def ajaxEvent():
    req = ajax.ajax()
    req.bind('complete', reqComplete)
    req.open('GET', "https://www.paxcorp.net/BrythonTakuzu/get_grid.php?taille=" + str(tailleTableau))
    req.send()


startGame("")

document["generate-button"].bind("click", generateEvent)
document["valider"].bind("click", verifEvent)
document["ajax-button"].bind("click", ajaxEvent)









