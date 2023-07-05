from enemigo import *
from item import *
from configuraciones import *
class Personaje_Enemigo_Secundario(Personaje_Enemigo):
    def __init__(self,nombre,vida,daño,velocidad_x,velocidad_y,potencia_salto,imagen,limit_velocidad_caida,x,y):
        super().__init__(vida,daño,velocidad_x,velocidad_y,potencia_salto,imagen,limit_velocidad_caida,x,y)
        self.nombre=nombre
