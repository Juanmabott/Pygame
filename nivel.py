import pygame
from configuraciones import *
from pygame.locals import *
from personaje_principal import *
from modo import *
from plataforma import *
from trampa import *
from enemigo import *
from item import *
from projectil import *
from interfaz import *
from spawnerEnemigo import *
from nivel import *
from constantes import *

class Nivel:
    def __init__(self,PANTALLA):
        self.lista_items_puntos = []
        self.lista_items_curacion=[]
        self.lista_plataforma = []
        self.lista_enemigos=[]
        self.enemigos_restantes = 9
        self.contador_enemigos_derrotados=0
        self.lugar_spawn_enemigos="derecha"
        
        self.barra_vida=Interfaz(corazones[0],10,10,PANTALLA)

        self.projectil=Projectil(projectil_agua,10,1000,1000)
        

        self.lista_plataforma.append(Plataforma(plataforma_tierra,"visible",PANTALLA,(ANCHO/2) ,(ALTO/2)))
        self.lista_plataforma.append(Plataforma(plataforma_tierra,"visible",PANTALLA,(ANCHO/2-400),(ALTO/2+200)))
        self.lista_plataforma.append(Plataforma(piso_tierra,"visible",PANTALLA,(ANCHO-ANCHO),(ALTO/2+350)))
        self.lista_plataforma.append(Plataforma(piso_tierra,"visible",PANTALLA,(ANCHO-ANCHO),(ALTO/2+350)))
        self.lista_plataforma.append(Plataforma(plataforma_tierra,"visible",PANTALLA,(ANCHO/2-800),(ALTO/2+100)))

        self.personaje_principal=Personaje_principal(velocidad_x,
                                        velocidad_y,
                                        potencia_salto,
                                        lista_animaciones,
                                        limit_velocidad_caida,
                                        gravedad,
                                        x_inicial,
                                        y_inicial)
        
        self.personaje_enemigo=Personaje_Enemigo(50,10,
                                        0,
                                        60,
                                        enemigo_camina,
                                        1,
                                        ANCHO,
                                        761
                                        )
        
        self.trampa=Trampa(trampa_espinas[0],"visible",PANTALLA, (ANCHO-210), ALTO/2+400)
        self.lista_items_curacion.append(Item(100,corazones_vida_chicos,PANTALLA,(1000),(ALTO/2-50)))
        self.lista_enemigos.append(self.personaje_enemigo)

    def spawnear_enemigos(self,personaje_enemigo):
        self.lugar_spawn_enemigos==("derecha")
        print(self.contador_enemigos_derrotados)
        if self.contador_enemigos_derrotados%10 == 0 and  self.contador_enemigos_derrotados!=0:
            #print(self.contador_enemigos_derrotados)
            if self.lugar_spawn_enemigos=="izquierda":
                self.lugar_spawn_enemigos="derecha"
            else:
                self.lugar_spawn_enemigos = "izquierda"
            self.contador_enemigos_derrotados+=1
            self.enemigos_restantes=10
            self.lista_enemigos.clear()
            
        if self.enemigos_restantes >0:
            for i in range(self.enemigos_restantes):
                if self.lugar_spawn_enemigos =="izquierda":
                    enemigo = Personaje_Enemigo(daño=personaje_enemigo.daño,
                                        velocidad_x=personaje_enemigo.velocidad_x,
                                        velocidad_y=personaje_enemigo.velocidad_y,
                                        potencia_salto=personaje_enemigo.potencia_salto,
                                        imagen=personaje_enemigo.imagen,
                                        limit_velocidad_caida=personaje_enemigo.limit_velocidad_caida,
                                        x=0,
                                        y=761)
                else:
                    enemigo = Personaje_Enemigo(daño=personaje_enemigo.daño,
                                        velocidad_x=personaje_enemigo.velocidad_x,
                                        velocidad_y=personaje_enemigo.velocidad_y,
                                        potencia_salto=personaje_enemigo.potencia_salto,
                                        imagen=personaje_enemigo.imagen,
                                        limit_velocidad_caida=personaje_enemigo.limit_velocidad_caida,
                                        x=1900,
                                        y=761)
                for lado in enemigo.rectangulo:
                    if i >0:
                        enemigo.rectangulo[lado].x = self.lista_enemigos[i-1].rectangulo[lado].x
                        enemigo.velocidad_x=self.lista_enemigos[i-1].velocidad_x*1.05
                        #enemigo.velocidad_x = self.lista_enemigos[i-1].velocidad_x*1.2
                    else:
                        enemigo.rectangulo[lado].x = enemigo.rectangulo[lado].x+50
                #print("hola")
                #enemigo.actualizar_rectangulos()
                
                self.lista_enemigos.append(enemigo)
                #print(len(self.lista_enemigos))
            self.enemigos_restantes=0

    def actualizar(self,screen,que_hace):
        self.personaje_principal = self.personaje_principal
        self.lista_enemigos = self.lista_enemigos

        self.plataformas = self.lista_plataforma
        self.personaje_principal.verificar_accion(que_hace,screen,self.lista_plataforma)
        self.personaje_principal.verificar_colision_enemigo(self.lista_enemigos)
        self.trampa.daniar_jugador(self.personaje_principal)  
        for enemigo in self.lista_enemigos:
            enemigo.mover_enemigo(screen,self.lista_plataforma,self.lista_items_puntos)
        for plataforma in self.plataformas:
            plataforma.draw(screen)
        for recompensa in self.lista_items_puntos:
            recompensa.draw(screen)
            recompensa.sumar_puntaje_personaje(self.personaje_principal)
        if self.contador_enemigos_derrotados<50:
            self.spawnear_enemigos(self.lista_enemigos[0])
        
            
        self.projectil.disparar_projectil(screen,self.personaje_principal,self.lista_enemigos,projectil_agua,self)
        
        self.barra_vida.animar_vida(corazones,screen,self.personaje_principal.vida)
        for curacion in self.lista_items_curacion:
            curacion.draw(screen)
            curacion.sumar_vida_personaje(self.personaje_principal)
        self.trampa.draw(screen)