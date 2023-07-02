import pygame
def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def reescalar_imagenes(lista_imagenes, ancho, alto):
    if type(lista_imagenes)==list:
        for i in range(len(lista_imagenes)):
            lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], (ancho, alto))
    else:
        lista_imagenes = pygame.transform.scale(lista_imagenes, (ancho, alto))
    return lista_imagenes

trampa_espinas=pygame.image.load("pygame/sources/escenario/trampas/Ceiling Trap - Level 2.png")



personaje_camina = [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/camina/0.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/camina/1.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/camina/2.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/camina/3.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/camina/4.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/camina/5.png")]

personaje_quieto= pygame.image.load("pygame/sources/magos/mago base/quieto/0.png")

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)

personaje_salta = pygame.image.load("pygame/sources/magos/mago base/quieto/0.png")

plataforma_tierra= pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/escenario/plataformas/plataforma_tierra.png")

#enemigo planta
enemigo_camina = [pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/0.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/1.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/2.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/3.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/4.png"),
                    pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/enemigo planta/walk separado/5.png")]

corazones_vida=pygame.image.load("pygame/sources/items/manzana.png")

projectil_agua=[pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/0.png"),
                pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/1.png"),
                pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/2.png"),
                pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/3.png"),
                pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/4.png"),
                pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/5.png"),
                pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/magos/mago base/projectil/6.png")]

corazones=[pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/items/0.png"),
           pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/items/1.png"),
           pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/items/2.png")]