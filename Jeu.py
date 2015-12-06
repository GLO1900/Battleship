import Model
import View
import Controller
from Joueur import Joueur
from Bateau import Bateau

class Jeu:
    #la class Main du projet
    #contient le MVC
    """ En temps normal, le model contient toute l'info (les joueurs, grille, bateau, etc...
    ensuite, la view s'update au model, donc ta view doit prendre en consideration les elements du model
    a afficher. exemple : la view doit afficher la grille d'un joueur, si la grille du joueur dans la model
    est egal a -1, cela veux dire qu'il y avait un bateau a cette endroit mais qu'il a deja ete toucher.
    aller voir dans grille pour les autres valeurs
    """
    def __init__(self):
        self.model = Model()
        self.view = View(self.model)
        self.controller = Controller(self.model, self.view)

if __name__ == "__main__":
    """
    Les lignes qui suivent representent une boucle de jeu fonctionnel, il va falloir l'adapter pour que les inputs
    soit sur l'interface graphique
    """
    #initialisation des joueurs et de la liste de joueurs
    j = Joueur('Jeff')
    g = Joueur('Gab')
    listJoueur = []
    listJoueur.append(j)
    listJoueur.append(g)
    turn = 0
    #la boucle qui dit: tant que les 2 joueurs de sont pas mort
    while(not(j.isDead()) and not(g.isDead())):
        #si c'est le premier tour, les joueurs place leur bateau
        if turn == 0:
            for j in listJoueur:
                j.placerBateau
            turn += 1
        else:
            #maintenent que les bateau sont placer, les joueurs doivent ecrire une posisiont en x et y a attaquer
            for j in range(len(listJoueur)):
                x1 = input('En quelle position en X voulez vous attaquer ? :')
                y1 = input('En quelle position en Y voulez vous attaquer ? :')
                x = int(x1)
                y = int(y1)
                #ici on determine quel joueur sera la cible de l'attaque
                if j == 0:
                    z = 1
                else:
                    z = 0
                j.attaquer((x, y), listJoueur[z])
            turn += 1

    #on affiche le gagnant
    for j in listJoueur:
        if not(j.isDead()):
            print(j + 'WON !!')
