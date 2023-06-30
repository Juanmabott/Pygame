from objeto_juego import *

class Projectil(Objeto_juego):
    def __init__(self,imagen,velocidad,x,y):
        super().__init__(imagen,x,y)
        self.velocidad = velocidad
        self.disparo=False
        self.tiempo=0
    def disparar_projectil(self,screen,personaje_principal,lista_enemigos,lista_imaegenes):   
        if self.disparo:
            if self.tiempo==0:
                self.rectangulo["main"]= personaje_principal.rectangulo["left"]
                self.actualizar_rectangulos()
            self.tiempo +=1    
            self.mover(self.velocidad,"x")
            self.actualizar_rectangulos()
            self.animar_projectil(screen,lista_imaegenes,lista_enemigos)
        if self.tiempo>= 60:
            self.disparo= False
            self.tiempo = 0  
            self.mover(1000,"y")
            self.disparo=False
            self.actualizar_rectangulos()


    def animar_projectil(self,screen,lista_imagenes,lista_enemigos):
        if isinstance(lista_imagenes,list):
            largo = len(lista_imagenes)-1
            if self.contador_pasos > largo: 
                self.contador_pasos = 0
            screen.blit(lista_imagenes[self.contador_pasos], self.rectangulo["main"])
            self.contador_pasos += 1
        else:
            screen.blit(lista_imagenes, self.rectangulo["main"])
        for enemigo in lista_enemigos:
            if self.rectangulo["main"].colliderect(enemigo.rectangulo["main"]):
                screen.blit(lista_imagenes[largo-1], self.rectangulo["main"])
                enemigo.vida="muerto"
