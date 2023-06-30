from objeto_juego import *

class Plataforma(Objeto_juego):
    def __init__(self,imagen,estado,screen,x,y):
        super().__init__(imagen,x,y)
        if estado== "visible":
            self.draw(screen)