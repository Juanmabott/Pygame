from nivel import *
from formulario import *
from nivel2 import *
from nivel3 import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/botta/Documents/pyton/pygame/sources/sonidos/tema_principal.mp3")

window_width = 800
window_height = 600



window = pygame.display.set_mode((window_width, window_height))
verde_oscuro = (0, 100, 0)
imagen_verde = pygame.Surface((1, 1))
imagen_verde.fill(verde_oscuro)
window.blit(imagen_verde, (0, 0))

RELOJ =pygame.time.Clock()

form1 = Form("jugar",window, 300 , window_height // 2 - 75, 200, 50, (165, 42, 42), (0, 0, 255), active=True,visible="visible",imagen = "C:/Users/botta/Documents/pyton/pygame/sources/menu/letras blancas/menu principal/jugar.png")
form2 = Form("opciones",window, 300 , window_height // 2, 200, 50, (165, 42, 42), (255, 0, 0), active=True,visible="visible",imagen = "C:/Users/botta/Documents/pyton/pygame/sources/menu/letras blancas/menu principal/opciones.png")
form3 = Form("salir",window, 300, window_height // 2 + 75, 200, 50, (165, 42, 42), (0, 255, 0), active=True,visible="visible",imagen = "C:/Users/botta/Documents/pyton/pygame/sources/menu/letras blancas/menu principal/salir.png")

formularios_menu= [form1, form2, form3]

form_level1 = Form("nivel1",window, 400, window_height // 2 - 75, 200, 50, (165, 42, 42), (0, 0, 255),active=False, visible="invisible",imagen = "pygame/sources/menu/letras blancas/numeros/1.png")
form_level2 = Form("nivel2",window, 400, window_height // 2, 200, 50, (165, 42, 42), (255, 0, 0), active=False, visible="invisible",imagen = "pygame/sources/menu/letras blancas/numeros/2.png")
form_level3 = Form("nivel3",window, 400, window_height // 2 + 75, 200, 50, (165, 42, 42), (0, 255, 0), active=False, visible="invisible",imagen = "pygame/sources/menu/letras blancas/numeros/3.png")

form_seleccion_level=[form_level1, form_level2, form_level3]

form_volumen_mas = Form("subirVolumen",window, 400, window_height // 2 - 75, 200, 50, (165, 42, 42), (0, 0, 255),active=False, visible="invisible",imagen = "pygame/sources/menu/letras blancas/numeros/1.png")
form_volumen_menos = Form("bajarVolumen",window, 400, window_height // 2, 200, 50, (165, 42, 42), (255, 0, 0), active=False, visible="invisible",imagen = "pygame/sources/menu/letras blancas/numeros/2.png")
form_volumen_switch = Form("cambiarVolumen",window, 400, window_height // 2 + 75, 200, 50, (165, 42, 42), (0, 255, 0), active=False, visible="invisible",imagen = "pygame/sources/menu/letras blancas/numeros/3.png")
form_volumen_salir = Form("salirVolumen",window, 400, window_height // 2 + 175, 200, 50, (165, 42, 42), (0, 255, 0), active=False, visible="invisible",imagen = "C:/Users/botta/Documents/pyton/pygame/sources/menu/letras blancas/menu principal/salir.png")
form_volumen_opciones=[form_volumen_mas,form_volumen_menos,form_volumen_switch,form_volumen_salir]

piso = pygame.Rect(0,ALTO/2+400, ANCHO, 20)
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Juego")

nivel_iniciado=False
bandera=False
bandera_opciones=False
run=True
bandera_jugar=False
bandera_menu=True

volumen_global=0.5
niveles_terminados=[0,0,0]

while run:
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()
    

    if not nivel_iniciado:  
        pygame.mixer.music.set_volume(volumen_global)
        pygame.mixer.music.play(loops=-1)


        if pygame.mouse.get_pressed()[0]:
            
            for form in formularios_menu:
                if bandera_menu:
                    if form.slave_rect.collidepoint(mouse_pos):
                        match(form.nombre):
                            case "jugar" :
                                if form.active:
                                    bandera_menu=False
                                    bandera_jugar=True
                            case "opciones" :
                                if form.active:
                                    bandera_jugar=False
                                    bandera_menu=False
                                    bandera_opciones=True
                            case "salir": 
                                if form.active:
                                    run=False
                    form.visible="visible"
                    form.set_active(True)
                else:
                    form.visible="invisible"
                    form.set_active(False)
            
            for formula in form_seleccion_level:
                if bandera_jugar:
                    if formula.clicked(mouse_pos):
                        match(formula.nombre):
                            case "nivel1" :
                                if formula.active:
                                    if niveles_terminados==[0,0,0]:
                                        bandera_menu=False
                                        bandera_jugar=True
                                        nivel_iniciado=True
                                        nivel_seleccionado=1
                            case "nivel2" :
                                    if niveles_terminados==[1,0,0]:
                                        bandera_menu=False
                                        bandera_jugar=True
                                        nivel_iniciado=True
                                        nivel_seleccionado=2
                            case "nivel3" :
                                    if niveles_terminados==[1,1,0]:
                                        bandera_menu=False
                                        bandera_jugar=True
                                        nivel_iniciado=True
                                        nivel_seleccionado=3
                    formula.visible="visible"
                    formula.set_active(True)
                else:
                    formula.visible="invisible"
                    formula.set_active(False)

            
            for ajustes in form_volumen_opciones:
                if bandera_opciones:
                    if ajustes.clicked(mouse_pos):
                        if ajustes.nombre=="subirVolumen":
                            if volumen_global<=1 and volumen_global>=0:
                                volumen_global+=0.1
                        elif ajustes.nombre=="bajarVolumen":
                            if volumen_global<=1 and volumen_global>=0:
                                volumen_global-=0.1
                                
                        elif ajustes.nombre=="cambiarVolumen":
                            if volumen_global>0:
                                volumen_global=0
                            else:
                                volumen_global=1
                        elif ajustes.nombre=="salirVolumen":
                            bandera_opciones=False
                            bandera_menu=True
                    ajustes.visible="visible"
                    ajustes.set_active(True)
                else:
                    ajustes.visible="invisible"
                    ajustes.set_active(False)
                
                    #form.set_active(True)
                    #nivel_iniciado = True 

    pygame.draw.rect(window, (0,0,0), (0, 0, window_width, window_height))
    for form in [form1, form2, form3, form_level1, form_level2, form_level3]+ form_volumen_opciones:
        if form.is_active() and form.visible == "visible":
            pygame.draw.rect(window, form.color_border, form.slave_rect, 3)
            form.draw()    
            window.blit(form.surface, (form.x, form.y))
        
            

    if nivel_iniciado:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                que_hace = "derecha"
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            que_hace = "izquierda"
        elif keys[pygame.K_SPACE]:
            que_hace = "salta"
        else:
            que_hace = "quieto"

    if nivel_iniciado and not bandera:
        match nivel_seleccionado:
            case 1:
                nivel=Nivel(volumen_global)
                bandera=True
            case 2:
                nivel=NivelDos(volumen_global)
                bandera=True
            case 3:
                nivel=NivelTres(volumen_global)
                bandera=True
            
    elif bandera:
        niveles=nivel.actualizar(que_hace)
        print(nivel.contador_enemigos_derrotados)
        match niveles:
            case 1:
                niveles_terminados=[1,0,0]
                nivel_seleccionado=2
                bandera=False
            case 2:
                niveles_terminados=[1,1,0]
                nivel_seleccionado=3
                bandera=False
            case 3:
                niveles_terminados=[1,1,1]
                bandera=False

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                nivel.projectil.disparo=True 

    pygame.display.update()
