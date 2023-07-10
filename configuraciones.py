import pygame
from constantes import *
def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    if isinstance(lista_original, list):
        for imagen in lista_original:
            lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    else:
        lista_girada.append(pygame.transform.flip(lista_original, flip_x, flip_y))
    
    return lista_girada

def reescalar_imagenes(lista_imagenes, ancho, alto):
    if type(lista_imagenes)==list:
        for i in range(len(lista_imagenes)):
            lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], (ancho, alto))
    else:
        lista_imagenes = pygame.transform.scale(lista_imagenes, (ancho, alto))
    return lista_imagenes

trampa_espinas=[pygame.image.load("pygame/sources/escenario/trampas/Ceiling Trap - Level 2.png")]

plataforma_tierra= pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/escenario/plataformas/plataforma_tierra.png")

#enemigo planta
enemigo_camina = [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/0.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/1.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/2.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/3.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/4.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/5.png")]

#enemigo lvl 2

enemigo_camina_lvl2 = [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo dos/0.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo dos/1.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo dos/2.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo dos/3.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo dos/4.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo dos/5.png")]

enemigo_camina_lvl2=reescalar_imagenes(enemigo_camina_lvl2,200,100)

enemigo_camina_lvl3 = [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo tres/0.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo tres/1.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo tres/2.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo tres/3.png")]




#personaje
personaje_quieto= [pygame.image.load("pygame/sources/magos/mago base/quieto/0.png")]

personaje_camina = [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/corre/0.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/corre/1.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/corre/2.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/corre/3.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/corre/4.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/corre/5.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/corre/6.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/corre/7.png")]

personaje_salta = [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/salta/0.png"),
                   pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/salta/1.png"),
                   pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/salta/1.png"),
                   pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/salta/1.png"),
                   ]

personaje_herido= [pygame.image.load("pygame/sources/magos/mago base/herido/0.png"),
                    pygame.image.load("pygame/sources/magos/mago base/herido/1.png")]

personaje_invencible = [pygame.image.load("pygame/sources/magos/mago base/quieto/1.png"),
                        pygame.image.load("pygame/sources/magos/mago base/quieto/0.png")]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)
#personaje 2

personaje_rayo_quieto= [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/quieto/0.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/quieto/1.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/quieto/2.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/quieto/3.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/quieto/4.png"),]

personaje_rayo_camina = [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/corriendo/0.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/corriendo/1.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/corriendo/2.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/corriendo/3.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/corriendo/4.png")]



personaje_rayo_camina_izquierda = girar_imagenes(personaje_rayo_camina, True, False)

personaje_rayo_salta = [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/salta/0.png"),
                   pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/salta/1.png"),
                   pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/salta/2.png"),
                   pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago rayo/salta/2.png"),
                   ]
#personaje 3 

personaje_fuego_quieto= [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago fuego/quieto/0.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago fuego/quieto/1.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago fuego/quieto/2.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago fuego/quieto/3.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago fuego/quieto/4.png"),]

personaje_fuego_camina = [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago fuego/corriendo/0.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago fuego/corriendo/1.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago fuego/corriendo/2.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago fuego/corriendo/3.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago fuego/corriendo/4.png")]

personaje_fuego_camina_izquierda = girar_imagenes(personaje_fuego_camina, True, False)

personaje_fuego_salta = [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago fuego/salta/0.png")]

personaje_quieto_izq=girar_imagenes(personaje_quieto,True,False)
personaje_rayo_quieto_izq=girar_imagenes(personaje_rayo_quieto,True,False)
personaje_fuego_quieto_izq=girar_imagenes(personaje_fuego_quieto,True,False)



lista_animaciones_fuego= [personaje_fuego_quieto, 
                            personaje_fuego_camina, 
                            personaje_fuego_salta, 
                            personaje_fuego_camina_izquierda,
                            personaje_invencible,
                            personaje_herido,personaje_fuego_quieto_izq]

corazones_vida=pygame.image.load("pygame/sources/items/manzana.png")

projectil_agua=[pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/0.png"),
                pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/1.png"),
                pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/2.png"),
                pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/3.png"),
                pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/4.png"),
                pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/5.png"),
                pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/6.png")]

projectil_rayo=[pygame.image.load("pygame/sources/magos/mago rayo/projectil/0.png"),
                pygame.image.load("pygame/sources/magos/mago rayo/projectil/1.png"),
                pygame.image.load("pygame/sources/magos/mago rayo/projectil/2.png"),]

projectil_fuego=[pygame.image.load("pygame/sources/magos/mago fuego/projectil/0.png"),
                pygame.image.load("pygame/sources/magos/mago fuego/projectil/1.png"),
                pygame.image.load("pygame/sources/magos/mago fuego/projectil/2.png")]

projectil_roca=[pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo tres/projectil/rock_round.png")]
projectil_roca=reescalar_imagenes(projectil_roca,200,200)

corazones=[pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/items/0.png"),
           pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/items/1.png"),
           pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/items/2.png")]

estrella=reescalar_imagenes(pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/items/star.png"),50,50)


piso_tierra=reescalar_imagenes(plataforma_tierra,ANCHO-200,100)

columna=[pygame.image.load("pygame/sources/escenario/plataformas/columna.png")]
columna=reescalar_imagenes(columna,200,400)

nivel_2_plataforma_normal=[pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/escenario/plataformas/twilight-tiles.png")]

nivel_2_plataforma=reescalar_imagenes(nivel_2_plataforma_normal,1900,100)

nivel_2_plataforma_normal=[pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/escenario/plataformas/twilight-tiles.png")]

corazones=reescalar_imagenes(corazones,150,50)

trampa_espinas=girar_imagenes(trampa_espinas,False,True)

trampa_espinas=reescalar_imagenes(trampa_espinas,200,50)

trampa_espinas=girar_imagenes(trampa_espinas,False,True)

corazones_vida_chicos=reescalar_imagenes(corazones_vida,50,50)
#girar_imagenes(enemigo_camina_lvl2,True,False)
lista_animaciones = [personaje_quieto, 
                        personaje_camina, 
                        personaje_salta, 
                        personaje_camina_izquierda,
                        personaje_invencible,
                        personaje_herido,personaje_quieto_izq]

lista_animaciones_rayo = [personaje_rayo_quieto, 
                            personaje_rayo_camina, 
                            personaje_rayo_salta, 
                            personaje_rayo_camina_izquierda,
                            personaje_invencible,
                            personaje_herido,personaje_rayo_quieto_izq]

#sonidos--------------------------------------------------------------------------------------------------------------------------------

