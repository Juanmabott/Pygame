import pygame
from pygame.locals import *

class Form():
    active_form = None
    def __init__(self,nombre,master_surface,x,y,w,h,color_background,color_border,active,visible,imagen):
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
        self.imagen= imagen
        self.x = x
        self.y = y
        self.visible= visible

        if(self.color_background != None):
            self.surface.fill(self.color_background)

    def set_active(self, activo):
        self.active = activo
    
    def is_active(self):
        return self.active
    def set_visible(self, visible):
        self.visible = visible
    def draw(self):
        self.surface.fill(self.color_background)
        if self.imagen:
            background_img = pygame.image.load(self.imagen)
            self.surface.blit(background_img, (50, 0))
        pygame.draw.rect(self.surface, self.color_border, self.slave_rect, 3)
    def clicked (self,mouse_pos):
        if self.slave_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                return True
    
