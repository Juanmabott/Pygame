from objeto_juego import *

class Projectil(Objeto_juego):
    def __init__(self,imagen,daño,velocidad,x,y):
        super().__init__(imagen,x,y)
        self.velocidad = velocidad
        self.disparo=False
        self.tiempo=0
        self.daño=daño
        self.direaccion="derecha"
    def disparar_projectil(self,screen,personaje_principal,lista_enemigos,lista_imaegenes,nivel,direccion):   
        if self.disparo:
            if self.tiempo==0 and self.disparo:
                self.rectangulo["main"]= personaje_principal.rectangulo["left"]
                self.actualizar_rectangulos()
            self.tiempo +=1
            if direccion=="quieto":    
                self.mover(self.velocidad,"x")
            else:
                self.mover(-self.velocidad,"x")
            self.actualizar_rectangulos()
            self.animar_projectil(screen,lista_imaegenes)
            for enemigo in lista_enemigos:
                if self.rectangulo["main"].colliderect(enemigo.rectangulo["main"]):
                    nivel.contador_enemigos_derrotados+=1
                    #print(nivel.contador_enemigos_derrotados)
                    enemigo.vida-=self.daño
                    self.disparo= False
                    self.tiempo = 0  
                    self.mover(1000,"y")
                    self.disparo=False
                    self.actualizar_rectangulos()
                    return True
        if self.tiempo>= 60:
            self.disparo= False
            self.tiempo = 0  
            self.mover(1000,"y")
            self.disparo=False
            self.actualizar_rectangulos()

    def disparar_projectil_enemigo(self,screen,personaje_principal,enemigo,lista_imaegenes,nivel):   
        if self.tiempo==0:
            self.rectangulo["main"]= enemigo.rectangulo["left"]
            self.actualizar_rectangulos()
        self.tiempo +=1
        if self.direaccion=="derecha":    
            self.mover(self.velocidad,"x")
            self.mover(-self.velocidad,"y")
        else:
            self.mover(-self.velocidad,"x")
            self.mover(-self.velocidad,"y")

        self.actualizar_rectangulos()
        self.animar_projectil(screen,lista_imaegenes)

        if self.rectangulo["main"].colliderect(personaje_principal.rectangulo["main"]):
            personaje_principal.vida-=self.daño
            print(personaje_principal.vida)
            self.disparo= False
            self.tiempo = 0  
            self.mover(1000,"y")
            self.disparo=False
            self.actualizar_rectangulos()

        if self.tiempo>= 60:
            if self.direaccion=="derecha":
                self.direaccion="izquierda"
            else:
                self.direaccion="derecha"
            self.disparo= False
            self.tiempo = 0  
            self.mover(1000,"y")
            self.disparo=False
            self.actualizar_rectangulos()

    def animar_projectil(self,screen,lista_imagenes):
        if isinstance(lista_imagenes,list):
            largo = len(lista_imagenes)-1
            if self.contador_pasos > largo: 
                self.contador_pasos = 0
            screen.blit(lista_imagenes[self.contador_pasos], self.rectangulo["main"])
            self.contador_pasos += 1
        else:
            screen.blit(lista_imagenes, self.rectangulo["main"])

