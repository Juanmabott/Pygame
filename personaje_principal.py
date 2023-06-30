from personaje import *
from configuraciones import *

class Personaje_principal(Personaje):
    def __init__(self,velocidad_x,velocidad_y,potencia_salto,imagen,limit_velocidad_caida,gravedad,x,y):
        super().__init__(velocidad_x,velocidad_y,potencia_salto,imagen,limit_velocidad_caida,x,y)
        self.en_contacto_con_plataforma=False
        self.__score=0
        self.gravedad= gravedad
        self.estasaltando=True
        self.vida=100
    def verificar_colision_enemigo(self, lista_de_enemigos):
        for enemigo in lista_de_enemigos:
            if self.rectangulo["main"].colliderect(enemigo.rectangulo["main"]):
                self.vida-=enemigo.daño

    def verificar_accion(self, accion_realizada,pantalla,piso,lista_plataformas):
        match accion_realizada:
            case "derecha":
                if not self.estasaltando:
                    self.animar_movimientos(pantalla,personaje_camina)
                self.mover(self.velocidad_x * +1,"x")
            
            case "izquierda":
                if not self.estasaltando:
                    self.animar_movimientos(pantalla,personaje_camina_izquierda)
                self.mover(self.velocidad_x * -1,"x")#decrementa en mover_pers

            case "salta":
                if not self.estasaltando : # para que solo salta una vez en la misma gravedad
                    self.estasaltando = True
                    self.saltar()
                    
            case "quieto":
                if not self.estasaltando:
                    self.animar_movimientos(pantalla, personaje_quieto)
        colision_con_plataforma = False  # Variable de bandera para controlar la colisión con alguna plataforma

        for plataforma in lista_plataformas:
            if self.verificar_colision_piso(piso) or self.verificar_colision(plataforma.rectangulo):
                if accion_realizada != "izquierda" and accion_realizada != "derecha":
                    self.animar_movimientos(pantalla,personaje_quieto)
                self.estasaltando = False
                self.en_contacto_con_plataforma = True
                colision_con_plataforma = True  # Se ha detectado una colisión con alguna plataform
        if not colision_con_plataforma:
            self.aplicar_gravedad(self.gravedad)
            self.animar_movimientos(pantalla, personaje_salta)
            self.estasaltando = True
        else:
            self.velocidad_y = 0

    def verificar_evento_personaje(self):
        pass