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
ANCHO,ALTO=1900,900
TAMAÑO_PANTALA=(ANCHO,ALTO)
FPS=18

lista_animaciones = [personaje_quieto, personaje_camina, 
                    personaje_salta, personaje_camina_izquierda]

pygame.init()
RELOJ =pygame.time.Clock()
PANTALLA= pygame.display.set_mode(TAMAÑO_PANTALA)

fondo=pygame.image.load("pygame\\sources\\fondos\\background0.png")
fondo = pygame.transform.scale(fondo,TAMAÑO_PANTALA)
PANTALLA.blit(fondo, (0,0))

gravedad = 5
potencia_salto = 60
limit_velocidad_caida = 15
esta_saltando = False
desplazamiento_y = 0

#_Personaje
x_inicial = ANCHO / 2 - 300
y_inicial = 650
pos_actual_x = 0
velocidad_x = 10
velocidad_y = 0

# rect_personaje = personaje_quieto[0].get_rect() 
# rect_personaje.x = x_inicial
# rect_personaje.y = y_inicial

# rect_enemigo = enemigo_camina[0].get_rect() 
# rect_enemigo.x = ANCHO / 2 - 300
# rect_enemigo.y = ALTO /2 + 350


# #plataforma
# x_inicial_plataforma = ANCHO/2
# y_inicial_plataforma = ALTO/2+200

# rect_plataforma = plataforma_tierra.get_rect()
# rect_plataforma.x = x_inicial_plataforma
# rect_plataforma.y = y_inicial_plataforma

# #plataforma 2   
# rect_plataforma_dos = plataforma_tierra.get_rect()
# rect_plataforma_dos.x = ANCHO/2 -400
# rect_plataforma_dos.y = ALTO/2+200

piso_tierra=reescalar_imagenes(plataforma_tierra,ANCHO,100)
# rect_plataforma_tres = piso_tierra.get_rect()
# rect_plataforma_tres.x = ANCHO-ANCHO
# rect_plataforma_tres.y = ALTO/2+350
corazones=reescalar_imagenes(corazones,150,50)

# rectangulos = obtener_rectangulo(rect_personaje)
# rectangulos_enemigo = obtener_rectangulo(rect_enemigo)
trampa_espinas=reescalar_imagenes(trampa_espinas,ANCHO/4,100)
# trampa_espinas=reescalar_imagenes(trampa_espinas, 200, 100)
# rect_trampa= trampa_espinas.get_rect()
# rect_trampa.x = ANCHO/2 -900
# rect_trampa.y = ALTO/2-100


personaje_principal=Personaje_principal(velocidad_x,
                                        velocidad_y,
                                        potencia_salto,
                                        lista_animaciones,
                                        limit_velocidad_caida,
                                        gravedad,
                                        x_inicial,
                                        y_inicial)

personaje_enemigo=Personaje_Enemigo(5,velocidad_x,
                                        velocidad_y,
                                        potencia_salto,
                                        enemigo_camina,
                                        limit_velocidad_caida,
                                        x_inicial+40,
                                        761
                                        )
spawner=SpawnerEnemigos(5)

piso = pygame.Rect(0,ALTO/2+400, ANCHO, 20)


#plataformas

# hitbox_plataforma= obtener_rectangulo(rect_plataforma)
# hitbox_plataforma_dos= obtener_rectangulo(rect_plataforma_dos) 
# hitbox_plataforma_tres= obtener_rectangulo(rect_plataforma_tres) 
#trampas
#hitbox_trampa=obtener_rectangulo(rect_trampa

lista_plataforma = []
lista_enemigos=[]

lista_enemigos.append(personaje_enemigo)
corazones_vida_chicos=reescalar_imagenes(corazones_vida,50,50)

trampa=Trampa(trampa_espinas,"visible",PANTALLA, (ANCHO/2), 10)
manzana=Item(100,corazones_vida_chicos,PANTALLA,(1000),(ALTO/2-50))

barra_vida=Interfaz(corazones[0],10,10,PANTALLA)

projectil=Projectil(projectil_agua,10,1000,1000)
run= True
while run:
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
            if event.type == pygame.QUIT:
                    run=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                        cambiar_modo()
    PANTALLA.blit(fondo,(0,0))
    keys=pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            que_hace = "derecha"
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        que_hace = "izquierda"
    elif keys[pygame.K_SPACE]:
        que_hace = "salta"
    else:
        que_hace = "quieto"
    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
            projectil.disparo=True  # Clic izquierdo del mouse

    plataforma = Plataforma(plataforma_tierra,"visible",PANTALLA,(ANCHO/2) ,(ALTO/2))
    plataforma_dos = Plataforma(plataforma_tierra,"visible",PANTALLA,(ANCHO/2-400),(ALTO/2+200))
    plataforma_tres = Plataforma(piso_tierra,"visible",PANTALLA,(ANCHO-ANCHO),(ALTO/2+350))       
    
    

    lista_plataforma.append(plataforma)
    lista_plataforma.append(plataforma_dos)
    lista_plataforma.append(plataforma_tres)
    # for plataforma in lista_plataforma:
    #     plataforma.draw(PANTALLA)
    pygame.draw.rect(PANTALLA, "yellow" , plataforma.rectangulo["main"], 1)
    if get_mode() == True: # dibuja rect piso y rect personaje
        pygame.draw.rect(PANTALLA, "Blue" , personaje_principal.rectangulo["main"], 1)
        pygame.draw.rect(PANTALLA, "red" , personaje_principal.rectangulo["bottom"], 5)
        pygame.draw.rect(PANTALLA, "yellow" , personaje_principal.rectangulo["top"], 5)
        pygame.draw.rect(PANTALLA, "yellow" , manzana.rectangulo["main"], 5)
        pygame.draw.rect(PANTALLA, "yellow" , projectil.rectangulo["main"], 5)

        pygame.draw.rect(PANTALLA, "red" , personaje_enemigo.rectangulo["main"], 1)
        # pygame.draw.rect(PANTALLA, "red" , rectangulos["left"], 1)
        # pygame.draw.rect(PANTALLA, "red" , redctangulos["right"], 1)
        # pygame.draw.rect(PANTALLA, "yellow" , rectangulos["top"], 1)
        # pygame.draw.rect(PANTALLA, "green" , rect_piso["main"], 1)

        # pygame.draw.rect(PANTALLA, "red" , hitbox_plataforma["top"], 1)
        #pygame.draw.rect(PANTALLA, "red" , plataforma_tres.rectangulos["main"], 1)
        for plataforma in lista_plataforma:
            pygame.draw.rect(PANTALLA, "yellow" , plataforma.rectangulo["main"], 1)

    enemigos = spawner.spawnear_enemigos(personaje_enemigo)
    projectil.disparar_projectil(PANTALLA,personaje_principal,lista_enemigos,projectil_agua)
    manzana.draw(PANTALLA)
    barra_vida.animar_vida(corazones,PANTALLA,personaje_principal.vida)
    manzana.sumar_vida_personaje(personaje_principal)
    trampa.daniar_jugador(personaje_principal)  
    personaje_principal.verificar_accion(que_hace,PANTALLA,lista_plataforma)
    personaje_enemigo.mover_enemigo(PANTALLA,lista_plataforma)
    personaje_principal.verificar_colision_enemigo(lista_enemigos)
    
    pygame.display.update()