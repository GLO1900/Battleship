from Bateau import Bateau
from Grille import Grille

class Joueur:
    #class qui represente le joueur, il possede ses bateau sa grille et tout
    def __init__(self, nom):
        self.listBateau = []
        self.initiationBateau()
        self.grille = Grille()
        self.nom = nom

    def getGrille(self):
        return self.grille

    #On initialise les bateau, comme mantionner dans la classe Bateau je pense qu'on peut enlever les tuple
    #qui representent les coordeonnees du bateau puisqu'il sont tous a 0
    def initiationBateau(self):
        self.listBateau = [Bateau('Contre-Torpilleur', 3, (0,0)),
                           Bateau('Torpilleur', 2, (0, 0)),
                           Bateau('Porte-Avions', 5, (0, 0)),
                           Bateau('Sous-Marin', 3, (0, 0)),
                           Bateau('Croiseur', 4, (0, 0))]

    #La fonction placeBateau demande 3 inputs, on doit changer ces inputs pour les attacher a l'interface graphique
    def placerBateau(self):
        #boucle pour chaque bateau dans la liste
        for b in self.listBateau:
            #tant que celui n'est pas placer sur la grille (le bateau est placer une fois que la position demander
            #est disponible
            while not b.estSurLaGrille():
                print('Placer votre : ' + b.nom)
                x = input('Position en X')
                y = input('Position en Y')
                o = input('Quel Orientation ? *4-Gauche, 8-Haut, 6-Droite, 2-Bas')

                #ici on regarde les inputs donner pour savoir si le bateau peut etre placer a cette endroit, si il peut
                #etre placer, on appel la fonction positionner de la class bateau, sinon on reprend de nouveaux inputs
                if (self.grille.isAvailable((x, y))):
                    if o == 4:
                        if y >= b.getLongueur:
                            for i in range(b.getLongueur):
                                if not(self.grille.isAvailable((x, y-i))):
                                    break
                            b.positionner((x, y), o)
                    elif o == 8:
                        if x >= b.getLongueur:
                            for i in range(b.getLongueur):
                                if not(self.grille.isAvailable((x-i, y))):
                                    break
                            b.positionner((x, y), o)
                    elif o == 6:
                        if y <= b.getLongueur:
                            for i in range(b.getLongueur):
                                if not(self.grille.isAvailable((x, y+i))):
                                    break
                            b.positionner((x, y), o)
                    elif o == 2:
                        if x <= b.getLongueurt:
                            for i in range(b.getLongueur):
                                if not(self.grille.isAvailable((x, y-i))):
                                    break
                            b.positionner((x, y), o)
                    else:
                        print('Le bateau ne peut pas etre positionner')


    #c'est la methode qui update tous les bateau sur la grille, en fait c'est cette methode qui change les valeurs de
    #la grille au point (x, y) pour mettre une reference vers le bateau
    def updateGrille(self):
        for b in self.listBateau:
            x = b.getCoord()[0]
            y = b.getCoord()[1]
            o = b.getOrientation()
            if o == 4:
                for i in range(b.getLongueur):
                    self.grille[x][y-i] = b
            if o == 8:
                for i in range(b.getLongueur):
                    self.grille[x-i][y] = b
            if o == 6:
                for i in range(b.getLongueur):
                    self.grille[x][y+i] = b
            if o == 2:
                for i in range(b.getLongueur):
                    self.grille[x+i][y] = b

    #La fonction attaquer prend une coordonnee a attaquer et un joueur a attaquer
    def attaquer(self, coord, joueur):
        if joueur.grille.isTouch(coord):
            joueur.getGrille().getBateau(coord).hit()
            if joueur.getGrille().getBateau(coord).getPv() <= 0:
                joueur.deleteBateau(joueur.getGrille().getBateau(coord))
            joueur.getGrille().setTableau2D(coord, -1)
        else:
            joueur.getGrille().setTableau2D(coord, -2)

    #un joueur est mort si il n'y a plus de bateau dans sa liste, un bateau est retirer de la liste lorsque celui-ci
    #est couler
    def isDead(self):
        if len(self.listBateau) == 0:
            return True
        else:
            return False
    #retire un bateau de la liste
    def deleteBateau(self, bateau):
        self.listBateau.remove(bateau)

    def __str__(self):
        string = ''
        string += self.nom

