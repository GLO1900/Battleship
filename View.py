import tkinter

class View():
    def __init__(self, model):
        #La view possede le model pour pouvoir afficher les donnee du model
        self.model = model