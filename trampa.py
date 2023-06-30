from plataforma import *

class Trampa(Plataforma):
    def __init__(self,imagen,estado,screen,x,y):
        super().__init__(imagen,estado,screen,x,y)
        self.danio=10
        if estado== "visible":
            self.draw(screen)

    def daniar_jugador(self,jugador):
        if self.rectangulo["bottom"].colliderect(jugador.rectangulo["main"]):
            jugador.vida-= self.danio
            print (jugador.vida)