class Controller:
    def __init__(self, model, view):
        #contient la view et le controller pour pouvoir les updater
        self.model = model
        self.view = view