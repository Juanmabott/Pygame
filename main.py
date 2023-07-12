from menu_funciones import *

warnings.simplefilter("ignore", category=Warning, append=True)

warnings.filterwarnings("ignore", category=UserWarning, message="libpng warning: iCCP: known incorrect sRGB profile")
warnings.filterwarnings("ignore", category=RuntimeWarning, message="libpng warning: .*")
warnings.filterwarnings("ignore", category=RuntimeWarning, message="libpng warning: iCCP: cHRM chunk does not match sRGB")
menu_principal=Menu()

RELOJ =pygame.time.Clock()

piso = pygame.Rect(0,ALTO/2+400, ANCHO, 20)

pygame.display.set_caption("Spell Casters")
run=True


menu_principal.nivel_iniciado=False
bandera=False
bandera_opciones=False

bandera_jugar=False
bandera_menu=True
data=[]
try:
    with open("saveGame","r") as file:
        encontrado=False
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i].startswith(menu_principal.nombre_jugador):
                datos=lines[i].split(",")
                puntaje_total=int(datos[1])
                encontrado=True
                niveles_terminados=[int(data.strip()) for data in datos[2:]]
                datos_jugador={"nombre":datos[0],"puntuacion":datos[1]}
                data.append(datos_jugador)
            else:
                datos=lines[i].split(",")
                datos_jugador={"nombre":datos[0],"puntuacion":datos[1]}
                data.append(datos_jugador)
        if not encontrado:
            niveles_terminados=[0,0,0]
            puntaje_total=0
            datos_jugador={"nombre":menu_principal.nombre_jugador,"puntuacion":puntaje_total}  
            data.append(datos_jugador)    
except FileNotFoundError:
    with open("saveGame","w") as file:
        niveles_terminados=[0,0,0]
        puntaje_total=0
        datos_jugador={"nombre":menu_principal.nombre_jugador,"puntuacion":puntaje_total}  
        data.append(datos_jugador) 

volumen_global=0.5
bandera_puntuacion=False
mira="derecha"
perdio=False


while run:
    posicion_y = 100

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
    

    if not menu_principal.nivel_iniciado:  
        pygame.mixer.music.set_volume(volumen_global)
        pygame.mixer.music.play(loops=-1)

        for form in menu_principal.formularios_menu:
            if bandera_menu:
                fondo=menu_principal.fondo
                if form.clicked(mouse_pos):
                    match(form.nombre):
                        case "jugar" :
                            if form.is_active():
                                bandera_menu=False
                                bandera_jugar=True
                        case "opciones" :
                            if form.is_active():
                                bandera_jugar=False
                                bandera_menu=False
                                bandera_opciones=True
                        case "salir": 
                            if form.is_active():
                                run=False
                        case "historia":
                            bandera_jugar=False
                            bandera_menu=False
                            fondo=pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/menu/letras blancas/menu principal/historia.jpg")
                            menu_principal.form5[0].set_active(True)
                            menu_principal.window.blit(fondo, (0, 0))
                        case "puntuacion" :
                            if form.is_active():
                                bandera_jugar=False
                                bandera_menu=False
                                bandera_puntuacion=True
                form.set_active(True)
            else:
                if menu_principal.form5[0].clicked(mouse_pos) and menu_principal.form5[0].is_active():
                    menu_principal.form5[0].set_active(False)
                    bandera_menu=True
                    fondo=menu_principal.fondo
                menu_principal.window.blit(fondo, (0, 0))
                form.set_active(False)
            
            for formula in menu_principal.form_seleccion_level:
                if bandera_jugar:
                    
                    menu_principal.salir_menu.set_active(True)
                    if  menu_principal.salir_menu.clicked(mouse_pos):
                            menu_principal.salir_menu.set_active(False)
                            bandera_jugar=False
                            bandera_menu=True
                    if formula.clicked(mouse_pos):
                        match(formula.nombre):
                            case "nivel1" :
                                if formula.active:
                                        bandera_menu=False
                                        bandera_jugar=False
                                        menu_principal.nivel_iniciado=True
                                        nivel_seleccionado=1
                            case "nivel2" :
                                    if niveles_terminados!=[0,0,0]:
                                        bandera_menu=False
                                        bandera_jugar=False
                                        menu_principal.nivel_iniciado=True
                                        nivel_seleccionado=2
                            case "nivel3" :
                                    if niveles_terminados==[1,1,0] or niveles_terminados==[1,1,1]:
                                        bandera_menu=False
                                        bandera_jugar=False
                                        menu_principal.nivel_iniciado=True
                                        nivel_seleccionado=3
                    formula.set_active(True)
                else:
                    formula.set_active(False)

            
            for ajustes in menu_principal.form_volumen_opciones: 
                if bandera_opciones and not bandera_menu:
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
                    ajustes.set_active(True)
                else:
                    ajustes.set_active(False)
                
                    #form.set_active(True)
                    #menu_principal.nivel_iniciado = True  
        if bandera_puntuacion:
            pygame.font.init()
            font = pygame.font.SysFont("Arial", 32)
            for jugador in data:
                nombre = jugador["nombre"]
                puntuacion = jugador["puntuacion"]

                nombre_texto = font.render(f"Nombre: {nombre}", True, (0, 0, 0))
                puntuacion_texto = font.render(f"Puntuación: {puntuacion}", True, (0, 0, 0))

                nombre_posicion = (menu_principal.window_width // 2 - nombre_texto.get_width() // 2, posicion_y)
                puntuacion_posicion = (menu_principal.window_width // 2 - puntuacion_texto.get_width() // 2, posicion_y + 50)

                menu_principal.window.blit(nombre_texto, nombre_posicion)
                menu_principal.window.blit(puntuacion_texto, puntuacion_posicion)
                menu_principal.salir_menu.set_active(True)
                if menu_principal.salir_menu.clicked(mouse_pos):
                    menu_principal.salir_menu.set_active(False)
                    bandera_menu=True
                    menu_principal.window.blit(menu_principal.fondo,(0,0))
                    bandera_puntuacion=False

                posicion_y += 100
            pygame.display.flip()
    #pygame.draw.rect(window, (0,0,0), (0, 0, window_width, window_height))
    for form in menu_principal.formularios_menu+menu_principal.form_seleccion_level+ menu_principal.form_volumen_opciones+menu_principal.form5+[menu_principal.salir_menu]:
        form.draw_if_active(menu_principal.window)
    
    if menu_principal.nivel_iniciado:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                que_hace = "derecha"
                mira="dercha"
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            que_hace = "izquierda"
            mira="izquierda"
        elif keys[pygame.K_SPACE]:
            que_hace = "salta"
            
        elif mira=="izquierda":
            que_hace= "quieto_izquierda"
        else:
            que_hace = "quieto"

    if (menu_principal.nivel_iniciado and not bandera):
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
            
    if perdio:
        window = pygame.display.set_mode((menu_principal.window_width, menu_principal.window_height))
        menu_principal.nivel_iniciado=False
        bandera=False
        bandera_opciones=False

        bandera_jugar=False
        bandera_menu=True

        volumen_global=0.5

        perdio=False
        
    elif bandera:
        niveles=nivel.actualizar(que_hace,mouse_pos)
        if 'nivel_terminado' in niveles:
            nivel_terminado = niveles['nivel_terminado']
            if nivel_terminado == 1:
                niveles_terminados = [1, 0, 0]
                nivel_seleccionado = 2
                bandera = False
                puntaje_total+=niveles['puntuacion']
            elif nivel_terminado == 2:
                niveles_terminados = [1, 1, 0]
                nivel_seleccionado = 3
                bandera = False
                puntaje_total+=niveles['puntuacion']
                
            elif nivel_terminado == 3:
                niveles_terminados = [1, 1, 1]
                bandera = False
                bandera_menu=True
                menu_principal.nivel_iniciado=False
                puntaje_total+=niveles['puntuacion']
            elif nivel_terminado == "perdio":
                perdio = True

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                nivel.projectil.disparo=True 
    
 

    with open("saveGame", "r") as file:
        lines = file.readlines()

        encontrado = False
        for i in range(len(lines)):
            if lines[i].startswith(menu_principal.nombre_jugador + ","):
                lines[i] = menu_principal.nombre_jugador + "," + str(puntaje_total) + "," + ",".join(map(str, niveles_terminados)) + "\n"
                encontrado = True
                break
        if not encontrado:
            lines.append(menu_principal.nombre_jugador + "," + str(puntaje_total) + "," + ",".join(map(str, niveles_terminados)) + "\n")

    with open("saveGame", "w") as file:
        file.writelines(lines)

    pygame.display.update()

