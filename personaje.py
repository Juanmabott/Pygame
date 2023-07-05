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
        retorno=False
        if self.rectangulo['bottom'].colliderect(plataforma['top']):
            retorno= True
            self.en_contacto_con_plataforma = True
            self.rectangulo['main'].bottom = plataforma['top'].top+2
            self.actualizar_rectangulos()
            
        elif self.rectangulo['top'].colliderect(plataforma['bottom']):
            
            retorno= 1
            self.rectangulo['main'].top = plataforma['main'].bottom+10 
            self.actualizar_rectangulos()
            
        elif self.rectangulo['main'].colliderect(plataforma['left']):
            retorno= 2
            self.rectangulo['main'].right = plataforma['left'].left-8
            self.actualizar_rectangulos()
            
        elif self.rectangulo['main'].colliderect(plataforma['right']):
            retorno= 3
            self.rectangulo['main'].left = plataforma['right'].right+8
            self.actualizar_rectangulos()
            
        return retorno
        
    def verificar_colision_enemigo(self):
        pass
    def lanzar_proyectil(self):
        pass
