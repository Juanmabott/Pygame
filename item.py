from plataforma import *

class Item(Plataforma):#es el hijo de objeto_juego
    def __init__(self,valor,imagen,estado,pantalla,x,y):
        super().__init__(imagen,estado,pantalla,x,y)
        self.valor = valor
        self.curacion = 100
        self.pantalla = pantalla
    
    def sumar_vida_personaje(self, personaje):
        if self.rectangulo['main'].colliderect(personaje.rectangulo['main']):
            self.en_contacto_con_personaje = True
            personaje.vida += self.valor
            self.rectangulo['main'].y = self.rectangulo['main'].y +1000

            self.draw(self.pantalla)
            return True
        else:
            self.en_contacto_con_personaje = False
    def sumar_puntaje_personaje(self, personaje):
        if self.rectangulo['main'].colliderect(personaje.rectangulo['main']):
            self.en_contacto_con_personaje = True
            self.curacion = 30
            personaje.__score += self.curacion
            self.rectangulo['main'].y = 1000
            self.draw(self.pantalla)
            return True
        else:
            self.en_contacto_con_personaje = False