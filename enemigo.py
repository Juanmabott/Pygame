from personaje import *

class Personaje_Enemigo(Personaje):
    def __init__(self,daño,velocidad_x,velocidad_y,potencia_salto,imagen,limit_velocidad_caida,x,y):
        super().__init__(velocidad_x,velocidad_y,potencia_salto,imagen,limit_velocidad_caida,x,y)
        self.en_contacto_con_plataforma=False
        self.girando=False
        self.daño=daño
        self.vida="vivo"
    def mover_enemigo(self,pantalla,lista_plataformas):
        bandera=False
        for plataforma in lista_plataformas:
            if self.verificar_colision(plataforma.rectangulo):
                bandera=True
        if bandera==True:
            self.velocidad_y=0
        else:
            self.aplicar_gravedad(1)
        for lado in self.rectangulo:       
            if self.rectangulo[lado].x < 100:
                self.velocidad_x=self.velocidad_x*-1
            elif self.rectangulo[lado].x > 1900 - 80:
                self.velocidad_x=self.velocidad_x*-1
        if self.vida=="vivo":
            self.mover(self.velocidad_x,"x")
            if self.velocidad_x > 0 and not self.girando:
                self.imagen=girar_imagenes(self.imagen,True,False)
                self.girando=True
            elif self.velocidad_x < 0 and self.girando:
                self.imagen=girar_imagenes(self.imagen,True,False)
                self.girando=False
            self.animar_movimientos(pantalla,self.imagen)
        else:
            self.mover(10000,"y")