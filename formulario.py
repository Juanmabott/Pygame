import pygame
from pygame.locals import *
import csv
import os

class Form():
    active_form = None
    def __init__(self,nombre,master_surface,x,y,w,h,color_background,color_border,active,imagen):
        self.nombre= nombre
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.imagen= pygame.image.load(imagen)
        self.x = x
        self.y = y

        if self.color_background==None:
            self.surface.set_colorkey(None)
        else:
            self.surface.fill(self.color_background)
        

    def set_active(self, activo):
        self.active = activo
    
    def is_active(self):
        # if(self.active):
        #     print(self.nombre)
        return self.active
    def set_visible(self, visible):
        self.visible = visible
    def draw(self):

        if self.color_background==None:
            self.surface.set_colorkey(None)
        else:
            self.surface.fill(self.color_background)

        if self.imagen:
            background_img = self.imagen
            self.surface.blit(background_img, (0, 0))
        #pygame.draw.rect(self.surface, self.color_border, self.slave_rect, 3)

    def clicked (self,mouse_pos):
        if self.slave_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                return True

    def draw_if_active(self,pantalla):
        if self.is_active():
            self.draw()    
            pantalla.blit(self.surface, (self.x, self.y))

    def ingresar_nombre_jugador(self,window):
        nombre_jugador=""

        input_rect=pygame.Rect(300,200,200,36)
        color_fondo_input=pygame.Color('black')
        font = pygame.font.Font(None,32)
        input_active=True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        input_active=False
                    else:
                        input_active=True
                if event.type== pygame.KEYDOWN:
                    if input_active:
                        if event.key == pygame.K_RETURN:
                            return nombre_jugador
                        elif event.key==pygame.K_BACKSPACE:
                            nombre_jugador=nombre_jugador[:-1]
                        else:
                            nombre_jugador+=event.unicode
                
                window.blit(self.imagen, (0,0))
                titulo=font.render("Ingrese su nombre",True,(255,0,0))
                window.blit(titulo, (self.w//2-titulo.get_width()//2, 0))

                pygame.draw.rect(window,color_fondo_input,input_rect)
                texto_ingresado= font.render(nombre_jugador,True,(255,0,255))
                window.blit(texto_ingresado,(input_rect.x+5,input_rect.y))

                pygame.display.flip()
