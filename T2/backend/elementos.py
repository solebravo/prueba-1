from abc import ABC, abstractmethod
from msvcrt import SEM_FAILCRITICALERRORS
import parametros as p
from PyQt5.QtCore import QObject



#Plantas
class PlantaClasica(QObject):
    def __init__(self):
        super().__init__()
        self.vida = p.VIDA_PLANTA
        self.intervalo = p.INTERVALO_DISPARO
        self.efecto = p.DANO_PROYECTIL

class PlantaAzul(QObject):
    def __init__(self):
        super().__init__()
        self.vida = p.VIDA_PLANTA
        self.intervalo = p.INTERVALO_DISPARO
        self.efecto = p.RALENTIZAR_ZOMBIE

class Girasol(QObject):
    def __init__(self):
        super().__init__()
        self.vida = p.VIDA_PLANTA
        self.intervalo = p.INTERVALO_SOLES_GIRASOL
        self.efecto = p.CANTIDAD_SOLES

class PlantaPatata(QObject):
    def __init__(self):
        super().__init__()
        self.vida = 2 * p.VIDA_PLANTA

#Zombies
class Zombie(QObject):
    def __init__(self):
        super().__init__()
        self.velocidad = 0
        self.dano = p.DANO_MORDIDA
        self.intervalo = p.INTERVALO_TIEMPO_MORDIDA
        self.vida = p.VIDA_ZOMBIE
     


class Tablero():
    def __init__(self):
        self.x_start = p.X_COMIENZO
        self.x_fin = p.X_FINAL
        self.y_up = p.Y_ARRIBA
        self.y_medio = p.Y_MEDIO
        self.y_down = p.Y_ABAJO
        self.lane = 0
        self.casilla = 0
    
    def casillas(self, x):
        size = p.TAMANO_CAS
        if  self.x_start < x < (self.x_start + size):
            self.casilla = self.x_start
        elif (self.x_start + size ) < x < (self.x_start + size * 2):
            self.casilla = self.x_start + size
        elif (self.x_start + size * 2 ) < x < (self.x_start + size * 3):
            self.casilla = self.x_start + size * 2
        elif (self.x_start + size * 3 ) < x < (self.x_start + size * 4):
            self.casilla = self.x_start + size * 3
        elif (self.x_start + size * 4 ) < x < (self.x_start + size * 5):
            self.casilla = self.x_start + size * 4
        elif (self.x_start + size * 5 ) < x < (self.x_start + size * 6):
            self.casilla = self.x_start + size * 5 
        elif (self.x_start + size * 6 ) < x < (self.x_start + size * 7):
            self.casilla = self.x_start + size * 6 
        elif (self.x_start + size * 7 ) < x < (self.x_start + size * 8):
            self.casilla = self.x_start + size * 7
        elif (self.x_start + size * 8 ) < x < (self.x_start + size * 9):
            self.casilla = self.x_start + size * 8
        elif (self.x_start + size * 9 ) < x < (self.x_start + size * 10):
            self.casilla = self.x_start + size * 9
        else:
            self.casilla = 'afuera'
        return self.casilla

    def lanes(self, y_):
        if y_ > self.y_up and y_ < self.y_medio:
            self.lane = self.y_up
        elif y_ > self.y_medio and y_ < self.y_down:
            self.lane = self.y_medio
        elif y_ < self.y_up or y_ > self.y_down:
            self.lane = 'afuera'
        return(self.lane)
        


      

    

    


    


    
    

