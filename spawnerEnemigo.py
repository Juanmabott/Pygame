
from enemigo import *

class SpawnerEnemigos:
    def __init__(self,cantidad_inicial):
        self.enemigos_restantes=cantidad_inicial

    def spawnear_enemigos(self,personaje_enemigo):
        enemigos = []
        if self.enemigos_restantes >0:
            for i in range(self.enemigos_restantes):
                enemigo=personaje_enemigo
                enemigos.append(enemigo)
            self.enemigos_restantes=0
        return enemigos
    
    def verificar_enemigos(self):
        if self.enemigos_restantes == 0:
            self.enemigos_restantes = 10 
