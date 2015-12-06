class Bateau():
    """
    un Bateau est construit avec un nom (string) une longueur(int) et une paire de coordonnee(tuple)
    je pense qu'on pourrait ne pas envoyer les coordonnee au constructeur puisque c'est toujours (0, 0)
    avant de les placer
    """
    def __init__(self, nom, longueur, coordonnee):
        self.nom = nom
        self.longueur = longueur
        self.coordonnee = coordonnee

        #l'orientation sert a determiner les autres coordonnees sur la grille
        #on utilise les numero sur le numpad : 4-Gauche, 8-Haut, 6-Droite, 2-Bas
        self.orientation = 0

        #on definie un boolean pour savoir si le bateau est sur la grille. dans la fonction 'placerBateau'
        #de la classe 'Joueur' on le met a true. On pourrait l'utiliser pour savoir si on affiche le bateau
        #sur la grille ou dans la banque de bateau a placer
        self.surLaGrille = False

        #pour l'affichage en ligne de commande la premiere lettre du bateau va servir a l'identifier
        self.representation = nom[0]

        #chaque fois qu'un bateau se fait attaque il perd 1 pv (point de vie) lorsqu'il tombe a 0 il est couler
        #le nombre de point de vie est donc necessairement = a sa longueur
        self.pv = longueur

    def positionner(self, coord, orientation):
        """
        ici on donne les coordonnees en tuple (x, y) au bateau. lorsqu'on positionne le bateau sur la grille,
        on prend son orientation et on met une reference vers le bateau a la coordonnee (x, y) puis autre autre
        coordonnee dependamment de l'orientation et de la longueur de celui-ci
        on met ensuite la variable : surLaGrille a True
        """

        self.coordonnee = coord
        self.orientation = orientation
        self.surLaGrille = True

    #fonction pour savoir si le bateau a ete placer sur la grille
    def estSurLaGrille(self):
        return self.surLaGrille

    def getLongueur(self):
        return self.longueur

    def getRepresentation(self):
        return self.representation

    def getCoord(self):
        return self.coordonnee

    def getOrientation(self):
        return self.orientation

    def getPv(self):
        return self.pv

    #fonction qui reduit les pv de 1, est appeller a chaque fois qu'on bateau est toucher
    def hit(self):
        self.pv -= 1

    def __str__(self):
        string = self.nom + ', ' + str(self.coordonnee) + ', ' + str(self.pv)
        return string