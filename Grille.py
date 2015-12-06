from Bateau import Bateau

DEFAULT_HEIGHT = 10
DEFAULT_WIDTH = 10

class Grille:
    def __init__(self):
        self.height = DEFAULT_HEIGHT
        self.width = DEFAULT_WIDTH
        self.tableau2D = []
        self.initiationTableau()

    def __str__(self):
        string = ''
        for i in range(len(self.tableau2D)):
            for j in range(len(self.tableau2D[i])):
                if j == (0):
                    string += '['
                if isinstance(self.tableau2D[i][j], Bateau):
                    string += self.tableau2D[i][j].getRepresentation()
                else:
                    string += str(self.tableau2D[i][j])
                if j != (len(self.tableau2D[i])-1):
                    string += ', '
                if j == (len(self.tableau2D[i])-1):
                    string += ']'
            if i != (len(self.tableau2D)-1):
                string += '\n'
        return string

    #change la valeur au point x, y du tableau AKA la grille
    def setTableau2D(self, coord, val):
        self.tableau2D[coord[0]][coord[1]] = val

    #on met toutes les valeurs du tableau a 0
    def initiationTableau(self):
        for i in range(self.height):
            listeH = []
            for j in range(self.width):
                listeH.append(0)
            self.tableau2D.append(listeH)

    #on verifie si un bateau est toucher, retourne True si un bateau est toucher
    #retourne false dans tous les autres cas, on pourrais faire afficher un popup qui dit couler, toucher ou rater ?
    def isTouch(self, coordo):
        coord = int(coordo)
        if isinstance(self.tableau2D[coord[0]][coord[1]], Bateau):
            return True
        elif self.tableau2D[coord[0]][coord[1]] == -1:
            print('Vous aviez deja toucher un bateau a cette endroit')
            return False
        elif self.tableau2D[coord[0]][coord[1]] == -2:
            print("Vous n'aviez rien toucher a cette endroit")
            return False
        elif self.tableau2D[coord[0]][coord[1]] == 0:
            print("Vous n'avez rien toucher")
            return False
        else:
            return False

    #regarde si la coordonnee est disponible pour mettre un bateau
    def isAvailable(self, coord):
        if int(coord[0]) > self.height or int(coord[0]) > self.width or int(coord[0]) < 0:
            return False
        if int(coord[1]) > self.height or int(coord[1]) > self.width or int(coord[1]) < 0:
            return False
        if self.tableau2D[int(coord[0])][int(coord[1])] == 0:
            return True
        else:
            return False

    def getBateau(self, coord):
        coordo = int(coord)
        return self.tableau2D[coordo[0]][coordo[1]]