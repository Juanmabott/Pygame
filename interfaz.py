from objeto_juego  import *

class Interfaz(Objeto_juego):
    def __init__(self,imagen,x,y,screen):
        super().__init__(imagen,x,y)
        self.draw(screen)
    def animar_vida(self,lista_imagenes,screen,dato,dato_actual):
        tercio= dato//3

        if  dato_actual<=tercio :
            frame=0
        elif  dato_actual<= tercio*2:
            frame=1
        elif dato_actual<=tercio*3:
            frame=2
        else:
            frame=2

        screen.blit(lista_imagenes[frame], self.rectangulo["main"])