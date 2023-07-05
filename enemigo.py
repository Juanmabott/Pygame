from personaje import *
from item import *
from configuraciones import *
class Personaje_Enemigo(Personaje):
    def __init__(self,vida,daño,velocidad_x,velocidad_y,potencia_salto,imagen,limit_velocidad_caida,x,y):
        super().__init__(velocidad_x,velocidad_y,potencia_salto,imagen,limit_velocidad_caida,x,y)
        self.en_contacto_con_plataforma=False
        self.girando=False
        self.daño=daño
        self.vida=vida
        self.estado="vivo"
    def mover_enemigo(self,pantalla,lista_plataformas,lista_items,lista_animaciones):
        if self.vida<=0:
            self.estado="muerto"

        choco_pilar=False
        bandera=False
        for plataforma in lista_plataformas:
            colision = self.verificar_colision(plataforma.rectangulo)
            
            if colision == 2 or colision == 3:
                choco_pilar = True
                
            if colision:
                bandera = True
        if bandera==True:
            self.velocidad_y=0
        else:
            self.aplicar_gravedad(1)
        for lado in self.rectangulo:       
            if self.rectangulo[lado].x < 100 or self.rectangulo[lado].x > 1900 - 80 or choco_pilar:           
                self.velocidad_x=self.velocidad_x*-1 
                
        if self.estado=="vivo":
            self.mover(self.velocidad_x,"x")
            
            if (self.velocidad_x > 0 and not self.girando) or (choco_pilar and not self.girando):
                self.imagen = girar_imagenes(lista_animaciones, True, False)
                self.girando = True
            elif self.velocidad_x < 0 and self.girando or (choco_pilar and self.girando):
                lista_animaciones = girar_imagenes(lista_animaciones, True, False)
                self.girando = False
            self.animar_movimientos(pantalla,lista_animaciones)
        elif self.rectangulo["main"].y < 10000:
            puntos = Item(100,estrella,pantalla,self.rectangulo["main"].x,self.rectangulo["main"].y)
            lista_items.append(puntos)
            bandera=True
            self.mover(10000,"y")
        else:
            self.mover(10000,"y")