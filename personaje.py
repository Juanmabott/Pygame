from objeto_juego import *


class Personaje(Objeto_juego):
    def __init__(self,velocidad_x,velocidad_y,potencia_salto,imagen,limit_velocidad_caida,x,y):
        super().__init__(imagen,x,y)
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y
        self.potencia_salto = potencia_salto
        self.limit_velocidad_caida= limit_velocidad_caida
        self.limit_velocidad_salto = limit_velocidad_caida
    def aplicar_gravedad(self,gravedad):
            if (self.velocidad_y + gravedad) <= self.limit_velocidad_caida:
                self.velocidad_y += gravedad
            self.mover(self.velocidad_y,"y")
    def saltar(self):
        self.velocidad_y -= self.potencia_salto
        self.mover(self.velocidad_y,"y")
        
    def verificar_colision_piso(self, rect_piso):
        if self.rectangulo['bottom'].colliderect(rect_piso['top']):
            self.en_contacto_con_plataforma = True
            self.rectangulo['main'].bottom = rect_piso['top'].top+2
            self.actualizar_rectangulos()
            return True
        if self.rectangulo['main'].colliderect(rect_piso['top']):
            self.en_contacto_con_plataforma = True
            self.rectangulo['main'].bottom = rect_piso['top'].top+2
            self.actualizar_rectangulos()
            return True
        else:
            self.en_contacto_con_plataforma = False
            return False
            
    def verificar_colision(self, plataforma):
        if self.rectangulo['bottom'].colliderect(plataforma['top']):
            self.en_contacto_con_plataforma = True
            self.rectangulo['main'].bottom = plataforma['top'].top+2
            self.actualizar_rectangulos()
            
            return True
        elif self.rectangulo['main'].colliderect(plataforma['bottom']):
            self.rectangulo['main'].top = plataforma['bottom'].bottom 
            self.actualizar_rectangulos()
            return 1
        else:
            return False
        
    def verificar_colision_enemigo(self):
        pass
    def lanzar_proyectil(self):
        pass
