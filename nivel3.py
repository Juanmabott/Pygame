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
from enemigo_secundario import *
class NivelTres:
    def __init__(self,volumen_global):
        self.lista_items_puntos = []
        self.lista_items_curacion=[]
        self.lista_plataforma = []
        self.lista_enemigos=[]
        self.enemigos_restantes = 9
        self.contador_enemigos_derrotados=0
        self.tamaño_jefe=(100,50)
        self.lugar_spawn_enemigos="derecha"
        self.pantalla= pygame.display.set_mode(TAMAÑO_PANTALA)
        self.barra_vida=Interfaz(corazones[0],10,10,self.pantalla)
        self.paused= False
        self.objeto_tomo_fuego=[Objeto_juego(tomo_fuego,1000000,1000)]
        #self.personaje_enemigo.rectangulo["main"].x,self.personaje_enemigo.rectangulo["main"].y
        self.projectil=Projectil(projectil_fuego,10,40,1000,1000)
        self.fondo=pygame.image.load("pygame/sources/fondos/background_jungle.jpg")
        self.fondo = pygame.transform.scale(self.fondo,TAMAÑO_PANTALA)
        self.recompensa=False
        
        self.form_set_pausa = Form("set_pausa", self.pantalla, ANCHO - 200 - 10, 10, 200, 50, (165, 42, 42), (0, 0, 255), active=True, imagen="pygame/sources/menu/letras blancas/menu principal/salir.jpg")

        self.form_pausa = Form("pausa", self.pantalla, ANCHO/2, 10, 200, 50, (165, 42, 42), (0, 0, 255), active=False, imagen="pygame/sources/menu/letras blancas/menu principal/jugar.jpg")

        self.pantalla.blit(self.fondo, (0, 0))
        self.enemigo_camina_lvl3_tamaño=reescalar_imagenes(enemigo_camina_lvl3,100,50)
        self.lista_plataforma.append(Plataforma(nivel_2_plataforma_normal,"visible",self.pantalla,(ANCHO/2) ,(ALTO/2)))
        self.lista_plataforma.append(Plataforma(nivel_2_plataforma_normal,"visible",self.pantalla,(ANCHO/2-400),(ALTO/2+200)))
        self.lista_plataforma.append(Plataforma(piso_jungla,"visible",self.pantalla,(ANCHO-ANCHO),(ALTO/2+400)))
        self.lista_plataforma.append(Plataforma(arbol_jungla,"visible",self.pantalla,(ANCHO/2-800),(ALTO/2)))
        self.lista_plataforma.append(Plataforma(arbol_jungla,"visible",self.pantalla,(ANCHO/2+600),(ALTO/2)))
        #self.lista_plataforma.append(Plataforma(nivel_2_plataforma_normal,"visible",self.pantalla,(ANCHO/2-800),(ALTO/2+100)))

        self.personaje_principal=Personaje_principal(10,
                                        velocidad_y,
                                        potencia_salto,
                                        lista_animaciones_fuego,
                                        20,
                                        gravedad,
                                        x_inicial,
                                        y_inicial)
        
        self.personaje_enemigo=Personaje_Enemigo(1,999,0,
                                        0,
                                        60,
                                        self.enemigo_camina_lvl3_tamaño,
                                        1,
                                        1600,
                                        384
                                        )
        self.personaje_enemigo_secundario=Personaje_Enemigo_Secundario("secuaz",1,999,5,
                                0,
                                60,
                                enemigo_camina_lvl2,
                                1,
                                ANCHO/2,
                                761
                                )
        
        #self.trampa=Trampa(trampa_espinas[0],"visible",self.pantalla, (ANCHO-210), ALTO/2+400)
        self.lista_items_curacion.append(Item(100,corazones_vida_chicos,self.pantalla,(1000),(ALTO/2-50)))
        self.lista_enemigos.append(self.personaje_enemigo_secundario)
        self.lista_enemigos.append(self.personaje_enemigo)
        self.sonido_daño = pygame.mixer.Sound("C:/Users/botta/Documents/pyton/pygame/sources/sonidos/damage.mp3")
        self.sonido_puntos= pygame.mixer.Sound("C:/Users/botta/Documents/pyton/pygame/sources/sonidos/coin.mp3")
        self.sonido_daño.set_volume(volumen_global)
        self.sonido_puntos.set_volume(volumen_global)

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
            self.enemigos_restantes=5
            self.lista_enemigos.clear()
            
        if self.enemigos_restantes >0:
            for i in range(self.enemigos_restantes):
                if self.lugar_spawn_enemigos =="izquierda":
                    enemigo = Personaje_Enemigo_Secundario(nombre=personaje_enemigo.nombre,vida=personaje_enemigo.vida,daño=personaje_enemigo.daño,
                                        velocidad_x=personaje_enemigo.velocidad_x,
                                        velocidad_y=personaje_enemigo.velocidad_y,
                                        potencia_salto=personaje_enemigo.potencia_salto,
                                        imagen=personaje_enemigo.imagen,
                                        limit_velocidad_caida=personaje_enemigo.limit_velocidad_caida,
                                        x=ANCHO/2,
                                        y=761)
                else:
                    enemigo = Personaje_Enemigo_Secundario(nombre=personaje_enemigo.nombre,vida=personaje_enemigo.vida,daño=personaje_enemigo.daño,
                                        velocidad_x=personaje_enemigo.velocidad_x,
                                        velocidad_y=personaje_enemigo.velocidad_y,
                                        potencia_salto=personaje_enemigo.potencia_salto,
                                        imagen=personaje_enemigo.imagen,
                                        limit_velocidad_caida=personaje_enemigo.limit_velocidad_caida,
                                        x=ANCHO/2,
                                        y=ALTO/2)
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

            self.personaje_principal.verificar_accion(que_hace,self.pantalla,self.lista_plataforma,lista_animaciones_fuego)

            self.personaje_principal.verificar_colision_enemigo(self.lista_enemigos,self.sonido_daño)

            #self.trampa.daniar_jugador(self.personaje_principal) 
            
            if self.contador_enemigos_derrotados %2 and self.contador_enemigos_derrotados!=0:
                
                alto, ancho= self.tamaño_jefe
                alto=alto+40
                ancho=ancho+10
                self.enemigo_camina_lvl3_tamaño=reescalar_imagenes(self.enemigo_camina_lvl3_tamaño,alto,ancho)
            for enemigo in self.lista_enemigos:
                if hasattr(enemigo, 'nombre'):
                    enemigo.mover_enemigo(self.pantalla,self.lista_plataforma,self.lista_items_puntos,enemigo_camina_lvl2,Item(100,estrella,self.pantalla,enemigo.rectangulo["main"].x,enemigo.rectangulo["main"].y))
                else:
                    enemigo.mover_enemigo(self.pantalla,self.lista_plataforma,self.lista_items_puntos,self.enemigo_camina_lvl3_tamaño,Objeto_juego(tomo_fuego,enemigo.rectangulo["main"].x,enemigo.rectangulo["main"].y))
            
            for plataforma in self.plataformas:
                plataforma.draw(self.pantalla)
            
            for recompensa in self.lista_items_puntos:
                recompensa.draw(self.pantalla)
                if not isinstance(recompensa, Item ):
                    recompensa.draw(self.pantalla)
                    if self.personaje_principal.rectangulo["main"].colliderect(recompensa.rectangulo["main"]) and not isinstance(recompensa, Item ):
                        print("ganaste")
                        return {'nivel_terminado':3,
                        'puntuacion':self.personaje_principal._Item__score+self.contador_enemigos_derrotados*10
                        }
                else:
                    recompensa.sumar_puntaje_personaje(self.personaje_principal,self.sonido_puntos)

                    recompensa.draw(self.pantalla)
            self.spawnear_enemigos(self.personaje_enemigo_secundario)

            self.projectil.disparar_projectil(self.pantalla,self.personaje_principal,self.lista_enemigos,projectil_fuego,self,que_hace)
            
            self.barra_vida.animar_vida(corazones,self.pantalla,self.personaje_principal.vida_inicial,self.personaje_principal.vida)
            for curacion in self.lista_items_curacion:
                curacion.draw(self.pantalla)
                curacion.sumar_vida_personaje(self.personaje_principal)
                
            self.form_set_pausa.draw_if_active(self.pantalla)

            if self.form_set_pausa.clicked(mouse_pos):
                    self.form_set_pausa.set_active(False)
                    self.form_pausa.set_active(True)
                    self.paused=True
        
        font = pygame.font.Font(None, 36)
        texto_puntuacion = font.render("Puntuación: " + str(self.personaje_principal._Item__score), True, WHITE)
        texto_rect = texto_puntuacion.get_rect(center=(ANCHO // 2, ALTO-ALTO+10))
        self.pantalla.blit(texto_puntuacion, texto_rect)   

        if self.personaje_principal.vida<=0:
            return {'nivel_terminado':"perdio",
                    'puntuacion':0
                    }
        else:
            return {}

            #self.trampa.draw(self.pantalla)