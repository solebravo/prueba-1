from abc import ABC, abstractmethod
from copyreg import constructor
from funciones_funcionamiento import lector_objetos, diccionario
from random import randint
from parametros import PROB_EXITO_BAYA,PROB_EXITO_CARAMELO, PROB_EXITO_POCION \
    , GASTO_ENERGIA_BAYA, GASTO_ENERGIA_CARAMELO, GASTO_ENERGIA_POCION, AUMENTO_DEFENSA


class Objeto(ABC):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.costo = 0
        self.prob_exito = 0
        self.aumento_vida = 0
        self.aumento_ataque = 0
        self.aumento_defensa = 0

    @abstractmethod
    def aplicar(self):
        pass
    #sera una funcion donde se pedira que self.atributo aumente

class Baya(Objeto):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        
    def aplicar(self):
        self.aumento_vida  += randint(1, 10)
        self.costo += GASTO_ENERGIA_BAYA
        self.prob_exito = PROB_EXITO_BAYA

class Pocion(Objeto):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        
    def aplicar(self):
        self.aumento_ataque  += randint(1, 7)
        self.costo += GASTO_ENERGIA_POCION
        self.prob_exito = PROB_EXITO_POCION

class Caramelo(Objeto):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        
    def aplicar(self):
        self.aumento_vida  += randint(1, 10)
        self.aumento_ataque  += randint(1, 7)
        self.aumento_defensa += AUMENTO_DEFENSA
        self.costo += GASTO_ENERGIA_CARAMELO
        self.prob_exito = PROB_EXITO_CARAMELO


#poci = Pocion('restos', 'pocion')
#poci.aplicar()
#print(poci.aumento_ataque)




