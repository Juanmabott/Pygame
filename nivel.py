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
from formulario import *
import sys


class Nivel:
    def __init__(self,volumen_global):
        self.lista_items_puntos = []
        self.lista_items_curacion=[]
        self.lista_plataforma = []
        self.lista_enemigos=[]
        self.enemigos_restantes = 10
        self.contador_enemigos_derrotados=0
        self.lugar_spawn_enemigos="derecha"
        self.pantalla= pygame.display.set_mode(TAMAÑO_PANTALA)
        self.paused= False
        

        self.barra_vida=Interfaz(corazones[0],10,10,self.pantalla)

        self.projectil=Projectil(projectil_agua,100,10,1000,1000)
        self.fondo=pygame.image.load("pygame\\sources\\fondos\\background0.png")
        self.fondo = pygame.transform.scale(self.fondo,TAMAÑO_PANTALA)
        
        pygame.display.flip()

        self.form_set_pausa = Form("set_pausa", self.pantalla, ANCHO - 200 - 10, 10, 200, 50, (165, 42, 42), (0, 0, 255), active=True, imagen="pygame/sources/menu/letras blancas/menu principal/salir.jpg")

        self.form_pausa = Form("pausa", self.pantalla, ANCHO/2, 10, 200, 50, (165, 42, 42), (0, 0, 255), active=False, imagen="pygame/sources/menu/letras blancas/menu principal/jugar.jpg")

        self.lista_plataforma.append(Plataforma(plataforma_tierra,"visible",self.pantalla,(ANCHO/2) ,(ALTO/2)))
        self.lista_plataforma.append(Plataforma(plataforma_tierra,"visible",self.pantalla,(ANCHO/2-400),(ALTO/2+200)))
        self.lista_plataforma.append(Plataforma(piso_tierra,"visible",self.pantalla,(ANCHO-ANCHO),(ALTO/2+350)))
        self.lista_plataforma.append(Plataforma(piso_tierra,"visible",self.pantalla,(ANCHO-ANCHO),(ALTO/2+350)))
        self.lista_plataforma.append(Plataforma(plataforma_tierra,"visible",self.pantalla,(ANCHO/2-800),(ALTO/2+100)))

        self.personaje_principal=Personaje_principal(velocidad_x,
                                        velocidad_y,
                                        potencia_salto,
                                        lista_animaciones,
                                        limit_velocidad_caida,
                                        gravedad,
                                        x_inicial,
                                        y_inicial)
        
        self.personaje_enemigo=Personaje_Enemigo(100,100,10,
                                        0,
                                        60,
                                        enemigo_camina,
                                        1,
                                        ANCHO,
                                        761
                                        )
        
        self.trampa=Trampa(trampa_espinas[0],"visible",self.pantalla, (ANCHO-210), ALTO/2+400)
        self.lista_items_curacion.append(Item(100,corazones_vida_chicos,self.pantalla,(1000),(ALTO/2-50)))
        self.sonido_daño = pygame.mixer.Sound("C:/Users/botta/Documents/pyton/pygame/sources/sonidos/damage.mp3")
        self.sonido_puntos= pygame.mixer.Sound("C:/Users/botta/Documents/pyton/pygame/sources/sonidos/coin.mp3")
        self.sonido_daño.set_volume(volumen_global)
        self.sonido_puntos.set_volume(volumen_global)
    
    def spawnear_enemigos(self):
        self.lugar_spawn_enemigos==("derecha")
    
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
                    enemigo = Personaje_Enemigo(vida=self.personaje_enemigo.vida,
                                                daño=self.personaje_enemigo.daño,
                                        velocidad_x=self.personaje_enemigo.velocidad_x,
                                        velocidad_y=self.personaje_enemigo.velocidad_y,
                                        potencia_salto=self.personaje_enemigo.potencia_salto,
                                        imagen=self.personaje_enemigo.imagen,
                                        limit_velocidad_caida=self.personaje_enemigo.limit_velocidad_caida,
                                        x=10,
                                        y=761)
                else:
                    enemigo = Personaje_Enemigo(vida=self.personaje_enemigo.vida
                                                ,daño=self.personaje_enemigo.daño,
                                        velocidad_x=self.personaje_enemigo.velocidad_x,
                                        velocidad_y=self.personaje_enemigo.velocidad_y,
                                        potencia_salto=self.personaje_enemigo.potencia_salto,
                                        imagen=self.personaje_enemigo.imagen,
                                        limit_velocidad_caida=self.personaje_enemigo.limit_velocidad_caida,
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

    def actualizar(self,que_hace,mouse_pos):
    
        #self.pantalla.blit(texto_puntuacion, (10, 10))
        if self.paused:
            self.pantalla.blit(self.fondo, (0, 0))
            self.form_pausa.draw_if_active(self.pantalla)  
            if self.form_pausa.clicked(mouse_pos):
                self.form_pausa.set_active(False)
                self.form_set_pausa.set_active(True)
                self.paused=False
        else:
            self.pantalla.blit(self.fondo, (0, 0))
            self.personaje_principal = self.personaje_principal
            self.lista_enemigos = self.lista_enemigos

            self.plataformas = self.lista_plataforma
            self.personaje_principal.verificar_accion(que_hace,self.pantalla,self.lista_plataforma,lista_animaciones)
            self.personaje_principal.verificar_colision_enemigo(self.lista_enemigos,self.sonido_daño)
            self.trampa.daniar_jugador(self.personaje_principal)  
            for enemigo in self.lista_enemigos:
                enemigo.mover_enemigo(self.pantalla,self.lista_plataforma,self.lista_items_puntos,enemigo_camina,Item(100,estrella,self.pantalla,enemigo.rectangulo["main"].x,enemigo.rectangulo["main"].y))
            for plataforma in self.plataformas:
                plataforma.draw(self.pantalla)
            for recompensa in self.lista_items_puntos:
                recompensa.draw(self.pantalla)
                recompensa.sumar_puntaje_personaje(self.personaje_principal,self.sonido_puntos)
            if self.contador_enemigos_derrotados<50:
                self.spawnear_enemigos()

            self.projectil.disparar_projectil(self.pantalla,self.personaje_principal,self.lista_enemigos,projectil_agua,self,que_hace)
            
            self.barra_vida.animar_vida(corazones,self.pantalla,self.personaje_principal.vida_inicial,self.personaje_principal.vida)
            for curacion in self.lista_items_curacion:
                curacion.draw(self.pantalla)
                curacion.sumar_vida_personaje(self.personaje_principal)
            self.trampa.draw(self.pantalla)
            self.form_set_pausa.draw_if_active(self.pantalla)

            if self.form_set_pausa.clicked(mouse_pos):
                    self.form_set_pausa.set_active(False)
                    self.form_pausa.set_active(True)
                    self.paused=True
        font = pygame.font.Font(None, 36)
        texto_puntuacion = font.render("Puntuación: " + str(self.personaje_principal._Item__score), True, WHITE)
        texto_rect = texto_puntuacion.get_rect(center=(ANCHO // 2, ALTO-ALTO+10))

        self.pantalla.blit(texto_puntuacion, texto_rect)    
        print(self.contador_enemigos_derrotados)
        if self.contador_enemigos_derrotados>49:
            return {'nivel_terminado':1,
                    'puntuacion':self.personaje_principal._Item__score+self.contador_enemigos_derrotados*10
                    }
        elif self.personaje_principal.vida<=0:
            return {'nivel_terminado':"perdio",
                    'puntuacion':0
                    }
        else:
            return {}
            