from personaje import *

class Personaje_principal(Personaje):
    def __init__(self,velocidad_x,velocidad_y,potencia_salto,imagen,limit_velocidad_caida,gravedad,x,y):
        super().__init__(velocidad_x,velocidad_y,potencia_salto,imagen,limit_velocidad_caida,x,y)
        self.en_contacto_con_plataforma=False
        self._Item__score=0
        self.gravedad= gravedad
        self.estasaltando=True
        self.herido=False
        self.vida=300
        self.invencibilidad = 5
    def verificar_colision_enemigo(self, lista_de_enemigos,sonido_daño):
        for enemigo in lista_de_enemigos:
            if self.rectangulo["main"].colliderect(enemigo.rectangulo["main"]) and self.invencibilidad<=0:
                self.vida-=enemigo.daño
                self.invencibilidad = 300
                self.herido=True
                sonido_daño.play()
                pygame.time.wait(int(sonido_daño.get_length() * 50))
            elif self.invencibilidad>0:
                self.invencibilidad-=1
                #

    def verificar_accion(self, accion_realizada,pantalla,lista_plataformas,lista_animaciones):
        #print(self.vida)
        match accion_realizada:
            case "derecha":
                if not self.estasaltando:
                    self.animar_movimientos(pantalla,lista_animaciones[1])
                self.mover(self.velocidad_x * +1,"x")
            
            case "izquierda":
                if not self.estasaltando:
                    self.animar_movimientos(pantalla,lista_animaciones[3])
                self.mover(self.velocidad_x * -1,"x")

            case "salta":
                if not self.estasaltando and self.verificar_colision!= 1:
                    self.estasaltando = True
                    self.saltar()
            case "quieto_izquierda":
                if self.herido:
                    for i in range(20):
                        self.animar_movimientos(pantalla,lista_animaciones[5])
                    self.herido=False
                if self.invencibilidad>0:
                    self.animar_movimientos(pantalla,lista_animaciones[4])
                elif not self.estasaltando:
                    self.animar_movimientos(pantalla, lista_animaciones[6])     

            case "quieto":
                if self.herido:
                    for i in range(20):
                        self.animar_movimientos(pantalla,lista_animaciones[5])
                    self.herido=False
                if self.invencibilidad>0:
                    self.animar_movimientos(pantalla,lista_animaciones[4])
                elif not self.estasaltando:
                    self.animar_movimientos(pantalla, lista_animaciones[0])

        colision_con_plataforma = False  # Variable de bandera para controlar la colisión con alguna plataforma
            
        for plataforma in lista_plataformas:
            if self.verificar_colision(plataforma.rectangulo)==True:
                self.estasaltando = False
                self.en_contacto_con_plataforma = True
                colision_con_plataforma = True  # Se ha detectado una colisión con alguna plataform
            elif self.verificar_colision(plataforma.rectangulo)==1:
                self.aplicar_gravedad(self.gravedad)
                self.animar_movimientos(pantalla,lista_animaciones[2])
                self.estasaltando = True
        if not colision_con_plataforma :
            self.aplicar_gravedad(self.gravedad)
            self.animar_movimientos(pantalla,lista_animaciones[2])
            self.estasaltando = True
        else:
            self.velocidad_y = 0

    def verificar_evento_personaje(self):
        pass