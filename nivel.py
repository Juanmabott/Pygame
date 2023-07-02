
class Nivel:
    def __init__(self, personaje_principal, lista_enemigos, recompensas, trampas, plataformas):
        self.personaje_principal = personaje_principal
        self.lista_enemigos = lista_enemigos
        self.recompensas = recompensas
        self.trampas = trampas
        self.plataformas = plataformas

    def actualizar(self):
        self.personaje.actualizar()
        for enemigo in self.enemigos:
            enemigo.actualizar()
        for recompensa in self.recompensas:
            recompensa.actualizar()
        for trampa in self.trampas:
            trampa.actualizar()
