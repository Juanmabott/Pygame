from nivel import *

pygame.init()
RELOJ =pygame.time.Clock()
PANTALLA= pygame.display.set_mode(TAMAÑO_PANTALA)

fondo=pygame.image.load("pygame\\sources\\fondos\\background0.png")
fondo = pygame.transform.scale(fondo,TAMAÑO_PANTALA)
PANTALLA.blit(fondo, (0,0))

piso = pygame.Rect(0,ALTO/2+400, ANCHO, 20)

nivel=Nivel(PANTALLA)

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
            nivel.projectil.disparo=True 


    nivel.actualizar(PANTALLA,que_hace)
    
    
    pygame.display.update()


#print(personaje_principal.rectangulo['main'].x)
        # # for plataforma in lista_plataforma:
    # #     plataforma.draw(PANTALLA)
    # pygame.draw.rect(PANTALLA, "yellow" , plataforma.rectangulo["main"], 1)
    # if get_mode() == True: # dibuja rect piso y rect personaje
    #     # pygame.draw.rect(PANTALLA, "Blue" , personaje_principal.rectangulo["main"], 1)
    #     # pygame.draw.rect(PANTALLA, "red" , personaje_principal.rectangulo["bottom"], 5)
    # #     # pygame.draw.rect(PANTALLA, "yellow" , personaje_principal.rectangulo["top"], 5)
    # #     pygame.draw.rect(PANTALLA, "yellow" , manzana.rectangulo["main"], 5)
    # #     pygame.draw.rect(PANTALLA, "yellow" , projectil.rectangulo["main"], 5)

    # #     # pygame.draw.rect(PANTALLA, "red" , personaje_enemigo.rectangulo["main"], 1)
    # #     # pygame.draw.rect(PANTALLA, "red" , rectangulos["left"], 1)
    # #     # pygame.draw.rect(PANTALLA, "red" , redctangulos["right"], 1)
    # #     # pygame.draw.rect(PANTALLA, "yellow" , rectangulos["top"], 1)
    # #     # pygame.draw.rect(PANTALLA, "green" , rect_piso["main"], 1)

    # #     # pygame.draw.rect(PANTALLA, "red" , hitbox_plataforma["top"], 1)
    # #     #pygame.draw.rect(PANTALLA, "red" , plataforma_tres.rectangulos["main"], 1)
    # #     for plataforma in lista_plataforma:
    # #         pygame.draw.rect(PANTALLA, "yellow" , plataforma.rectangulo["main"], 1)
    # # #enemigos = spawner.spawnear_enemigos(personaje_enemigo)

    
    # #personaje_enemigo.mover_enemigo(PANTALLA,lista_plataforma)

    
    