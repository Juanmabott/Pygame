import pygame
from constantes import *
def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    if isinstance(lista_original, list):
        
        for imagen in lista_original:
            lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    else:
        lista_girada.append(pygame.transform.flip(lista_original, flip_x, flip_y))
        print("no es una lista")
    return lista_girada

def reescalar_imagenes(lista_imagenes, ancho, alto):
    if type(lista_imagenes)==list:
        for i in range(len(lista_imagenes)):
            lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], (ancho, alto))
    else:
        lista_imagenes = pygame.transform.scale(lista_imagenes, (ancho, alto))
    return lista_imagenes

trampa_espinas=[pygame.image.load("pygame/sources/escenario/trampas/Ceiling Trap - Level 2.png")]



# personaje_camina = [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/camina/0.png"),
#                     pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/camina/1.png"),
#                     pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/camina/2.png"),
#                     pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/camina/3.png"),
#                     pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/camina/4.png"),
#                     pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/camina/5.png")]

plataforma_tierra= pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/escenario/plataformas/plataforma_tierra.png")


#enemigo planta
enemigo_camina = [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/0.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/1.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/2.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/3.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/4.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/5.png")]
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
                pygame.image.load("pygame/sources/magos/mago rayo/projectil/2.png"),
]

corazones=[pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/items/0.png"),
           pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/items/1.png"),
           pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/items/2.png")]

estrella=reescalar_imagenes(pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/items/star.png"),50,50)

piso_tierra=reescalar_imagenes(plataforma_tierra,ANCHO-200,100)
corazones=reescalar_imagenes(corazones,150,50)
trampa_espinas=reescalar_imagenes(trampa_espinas,200,50)
trampa_espinas=girar_imagenes(trampa_espinas,False,True)

corazones_vida_chicos=reescalar_imagenes(corazones_vida,50,50)

lista_animaciones = [personaje_quieto, 
                        personaje_camina, 
                        personaje_salta, 
                        personaje_camina_izquierda,
                        personaje_invencible,
                        personaje_herido]

lista_animaciones_rayo = [personaje_rayo_quieto, 
                            personaje_rayo_camina, 
                            personaje_rayo_salta, 
                            personaje_rayo_camina_izquierda,
                            personaje_invencible,
                            personaje_herido]

#sonidos--------------------------------------------------------------------------------------------------------------------------------

