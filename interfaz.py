from objeto_juego  import *

class Interfaz(Objeto_juego):
    def __init__(self,imagen,x,y,screen):
        super().__init__(imagen,x,y)
        self.draw(screen)
    def animar_vida(self,lista_imagenes,screen,dato):
        tercio= dato/3
        if  dato>= tercio*2 :
            frame=2
        elif  dato>= tercio:
            frame=1
        else:
            frame=0

        screen.blit(lista_imagenes[frame], self.rectangulo["main"])