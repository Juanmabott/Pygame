from nivel import *
from formulario import *
from nivel2 import *
from nivel3 import *
import warnings

class Menu():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/botta/Documents/pyton/pygame/sources/sonidos/tema_principal.mp3")
        
        self.fondo=pygame.image.load("C:/Users/botta/Documents/pyton/pygame/sources/fondos/background1-720.png")  
        self.nivel_iniciado=False
        self.window_width = 800
        self.window_height = 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        self.form_pedir_nombre=Form("seleccionar_nombre",self.window, self.window_width//2 , self.window_height // 2 - 80, 100, 100, (0, 0, 0), (0, 0, 255), active=True,imagen = "C:/Users/botta/Documents/pyton/pygame/sources/fondos/background1-720.png")
        self.nombre_jugador=self.form_pedir_nombre.ingresar_nombre_jugador(self.window)
        self.window.blit( self.fondo, (0, 0))
        form1 = Form("jugar",self.window, 350 , self.window_height // 2 - 80, 100, 60, None, None, active=True,imagen = "C:/Users/botta/Documents/pyton/pygame/sources/menu/letras blancas/menu principal/jugar.jpg")
        form2 = Form("opciones",self.window, 350 , self.window_height // 2, 100, 60, (0, 0, 0), (255, 0, 0), active=True,imagen = "C:/Users/botta/Documents/pyton/pygame/sources/menu/letras blancas/menu principal/opciones.jpg")
        form3 = Form("salir",self.window, 350, self.window_height // 2 + 235, 100, 60, (0, 0, 0), (0, 255, 0), active=True,imagen = "C:/Users/botta/Documents/pyton/pygame/sources/menu/letras blancas/menu principal/salir.jpg")
        form4 = Form("historia",self.window, 350, self.window_height // 2 + 75, 100, 60, (0, 0, 0), (0, 0, 0), active=True,imagen = "C:/Users/botta/Documents/pyton/pygame/sources/menu/letras blancas/menu principal/historiaBottom.jpg")
        form6 = Form("puntuacion",self.window, 350, self.window_height // 2 + 155, 100, 60, (0, 0, 0), (0, 0, 0), active=True,imagen = "C:/Users/botta/Documents/pyton/pygame/sources/menu/letras blancas/menu principal/puntiaciones.jpg")
        self.salir_menu=Form("salirMenu",self.window, 10, self.window_height -150, 100, 50, (165, 42, 42), (0, 255, 0), active=False,imagen = "pygame/sources/menu/letras blancas/menu principal/salir.jpg")

        self.formularios_menu= [form1, form2, form3,form4,form6]

        form_level1 = Form("nivel1",self.window, 400, self.window_height // 2 - 75, 200, 50, (165, 42, 42), (0, 0, 255),active=False,imagen = "pygame/sources/menu/letras blancas/numeros/1.png")
        form_level2 = Form("nivel2",self.window, 400, self.window_height // 2, 200, 50, (165, 42, 42), (255, 0, 0), active=False,imagen = "pygame/sources/menu/letras blancas/numeros/2.png")
        form_level3 = Form("nivel3",self.window, 400, self.window_height // 2 + 75, 200, 50, (165, 42, 42), (0, 255, 0), active=False,imagen = "pygame/sources/menu/letras blancas/numeros/3.png")

        self.form_seleccion_level=[form_level1, form_level2, form_level3]

        form_volumen_mas = Form("subirVolumen",self.window, 400, self.window_height // 2 - 75, 200, 50, (165, 42, 42), (0, 0, 255),active=False,imagen ="pygame/sources/menu/letras blancas/menu principal/subirVolumen.jpg")
        form_volumen_menos = Form("bajarVolumen",self.window, 400, self.window_height // 2, 200, 50, (165, 42, 42), (255, 0, 0), active=False,imagen = "pygame/sources/menu/letras blancas/menu principal/bajarVolumen.jpg")
        form_volumen_switch = Form("cambiarVolumen",self.window, 400, self.window_height // 2 + 75, 200, 50, (165, 42, 42), (0, 255, 0), active=False,imagen = "pygame/sources/menu/letras blancas/menu principal/alternarVolumen.jpg")
        form_volumen_salir = Form("salirVolumen",self.window, 400, self.window_height // 2 + 175, 200, 50, (165, 42, 42), (0, 255, 0), active=False,imagen = "pygame/sources/menu/letras blancas/menu principal/salir.jpg")

        self.form_volumen_opciones=[form_volumen_mas,form_volumen_menos,form_volumen_switch,form_volumen_salir]

        self.form5 = [Form("salirhistoria",self.window, self.window_width//2, self.window_height // 2 + 200, 100, 60, (0, 0, 0), (0, 255, 0), active=False,imagen = "C:/Users/botta/Documents/pyton/pygame/sources/menu/letras blancas/menu principal/salir.jpg")]
