import pygame
from pygame.locals import *
from configuraciones import *
class Objeto_juego():
    contador_pasos = 0
    def __init__(self,imagen,x,y):
        self.imagen = imagen
        if isinstance(self.imagen, list):
            self.rectangulos = self.imagen[0].get_rect() 
            self.rectangulos.x = x
            self.rectangulos.y = y
        else:
            self.rectangulos = self.imagen.get_rect() 
            self.rectangulos.x = x
            self.rectangulos.y = y
        self.rectangulo = self.obtener_rectangulo(self.rectangulos)
    def draw(self,screen):
        screen.blit(self.imagen,self.rectangulo["main"])

    def mover(self,velocidad,condicion):
            if condicion == "x":
                for lado in self.rectangulo:
                    if self.rectangulo[lado].x >= 0 and self.rectangulo[lado].x <= (1900 - 80):
                        self.rectangulo[lado].x += velocidad
                    elif self.rectangulo[lado].x < 0:
                        self.rectangulo[lado].x = 0
                    elif self.rectangulo[lado].x > 1900 - 80:
                        self.rectangulo[lado].x = 1900 - 80
            if condicion == "y":
                    self.rectangulo['main'].y += velocidad
                    self.rectangulo['top'].y += velocidad
                    self.rectangulo['bottom'].y += velocidad
                    self.rectangulo['left'].y += velocidad
                    self.rectangulo['right'].y += velocidad

    def animar_movimientos(self,screen,lista_imagenes):
        if isinstance(lista_imagenes, list):
            largo = len(lista_imagenes)-1
            if self.contador_pasos > largo: 
                self.contador_pasos = 0
            screen.blit(lista_imagenes[self.contador_pasos], self.rectangulo["main"])
            self.contador_pasos += 1
        else:
            screen.blit(lista_imagenes, self.rectangulo["main"])

    def update():
        pass
    def obtener_rectangulo(self,principal):
        diccionario = {}
        diccionario['main'] = principal.copy()
        diccionario['bottom'] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
        diccionario['right'] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
        diccionario['left'] = pygame.Rect(principal.left, principal.top, 2 , principal.height)
        diccionario['top'] = pygame.Rect(principal.left, principal.top, principal.width, 10)

        return diccionario
    
    def actualizar_rectangulos(self):
        self.rectangulo['bottom'] = pygame.Rect(self.rectangulo['main'].left, self.rectangulo['main'].bottom - 10, self.rectangulo['main'].width, 10)
        self.rectangulo['right'] = pygame.Rect(self.rectangulo['main'].right - 2, self.rectangulo['main'].top, 2, self.rectangulo['main'].height)
        self.rectangulo['left'] = pygame.Rect(self.rectangulo['main'].left, self.rectangulo['main'].top, 2, self.rectangulo['main'].height)
        self.rectangulo['top'] = pygame.Rect(self.rectangulo['main'].left, self.rectangulo['main'].top, self.rectangulo['main'].width, 10)
        self.rectangulo['main'] = pygame.Rect(self.rectangulo['main'].left, self.rectangulo['main'].top, self.rectangulo['main'].width, self.rectangulo['main'].height)