from plataforma import *

class Trampa(Plataforma):
    def __init__(self,imagen,estado,screen,x,y):
        super().__init__(imagen,estado,screen,x,y)
        self.ultimo_lado="izquierda"
        self.danio=10
        if estado== "visible":
            self.draw(screen)

    def daniar_jugador(self,jugador):
        if self.rectangulo["bottom"].colliderect(jugador.rectangulo["main"]):
            jugador.vida-= self.danio
            print (jugador.vida)
    
    def mover_rango(self,rango_minimo,rango_maximo,velocidad,direccion):
        if direccion=="x":
            if self.rectangulo["main"].x<= rango_minimo :
                self.ultimo_lado="izquierda"
            elif self.rectangulo["main"].x>= rango_maximo:
                self.ultimo_lado="derecha"

            if self.ultimo_lado=="izquierda":
                self.mover(velocidad,"x")
            elif self.ultimo_lado=="derecha":
                self.mover(-velocidad,"x")