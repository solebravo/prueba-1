
from Entrenador import Entrenador
from funciones_funcionamiento import checkeador
from funciones_funcionamiento import lector_programones
from funciones_funcionamiento import diccionario_programones
import sys
from random import randint
from random import choice
from random import shuffle
from funciones_funcionamiento import diccionario


class LigaProgramon:
    def __init__(self, entrenadores_con_atributos, numero_entrenador, todos_entrenas=[]):
        entrenadores = []
        for entrena in entrenadores_con_atributos:
            entrenadores.append(entrena[0])
        self.entrenadores = entrenadores
        self.entrenadores_con_atributos = entrenadores_con_atributos
        self.entrenador_elegido = entrenadores_con_atributos[numero_entrenador]
        self.nombre_entrenador = entrenadores_con_atributos[numero_entrenador][0]
        self.numero_entrenador = numero_entrenador
        self.perdedores = []
        self.todos = todos_entrenas
        self.ronda_actual = 1
        self.campeon = 0

    def crear_entrenadores(self):
        entrenadores_instanciados = {}
        for entrena in range(len(self.entrenadores_con_atributos)):
            entrenador = Entrenador(self.entrenadores_con_atributos[entrena])
            entrenadores_instanciados[entrenador.nombre] = entrenador
        return entrenadores_instanciados

    #incompleta
    def resumen_campeonato(self):
        print('*RESUMEN CAMPEONATO*')
        print(f'Entrenadores participantes: {self.todos}')
        print(f"Ronda actual: {self.ronda_actual}")
        print(f'Entrenadores que siguen en competencia: {self.entrenadores}')
        
    def simular_ronda(self, dic_entrenas_progras_instanciados):

        programones = []
        for atributo in self.entrenadores_con_atributos[self.numero_entrenador][1]:
            programones.append(atributo)
        print('*ELIGE TU LUCHADOR*')
        for numero in range(len(programones)):
            print(f'[{numero}] {programones[numero]}')
            number = int(numero)
        print(f"[{number + 1}] Salir")

        #elegir programon
        numero_menu = input()
        while checkeador(len(programones) + 1, numero_menu) != True:
            print('El caracter que haz ingresado no corresponde'
            ' ha alguna accion conocida, porfavor ingresa '
            'otro numero')
            numero_menu = input()
        seleccion = int(numero_menu)
        if seleccion == number + 1:
            sys.exit()
        programon_elegido = self.entrenador_elegido[1][seleccion]
        atributos_programones = diccionario_programones()
        programon_elegido_atris = atributos_programones[programon_elegido]

        entrena = []
        progras = []
      
        entrenas_atris = []
        for atris in self.entrenadores_con_atributos:
            if atris[0] in dic_entrenas_progras_instanciados:
                entrenas_atris.append(atris)


        for lista in entrenas_atris:
            entrena.append(lista[0])
            posi = randint(0,len(lista[1]) - 1)
            progras.append(lista[1][posi])
        entrenadores_progras = list(zip(entrena, progras))

        #Duelos
        copia_progas = entrenadores_progras.copy()
        mitad = (len(entrenadores_progras)) / 2
        shuffle(copia_progas)
        jugadores_1 = copia_progas[:int(mitad)]
        jugadores_2 = copia_progas[int(mitad):]
        duelos = list(zip(jugadores_1, jugadores_2))
    
        #llamar luchar
        print()
        print(f'--RONDA {self.ronda_actual}--')
        ganadores = []
        for duelo in duelos:
            #duelo = dos entrenadores con su programon)
            resultado = {}
            for jugador in duelo:
                #lista entrena,programon
                entrena1 = jugador[0]
                jugador1 = dic_entrenas_progras_instanciados[jugador[0]][jugador[1]]
                puntaje_j1 = jugador1.luchar(duelo, atributos_programones )
            duelo_reverse= tuple(reversed(duelo))
            for  jugador in duelo_reverse:
                entrena2 = jugador[0]
                jugador2 = dic_entrenas_progras_instanciados[jugador[0]][jugador[1]]
                puntaje_j2 = jugador2.luchar(duelo_reverse, atributos_programones )
            mayor = max(int(puntaje_j1),int(puntaje_j2))
            
            if mayor == int(puntaje_j1):
                ganador = entrena1
                perdedor = entrena2
                self.perdedores.append(perdedor)
                ganadores.append(ganador)
            else:
                ganador = entrena1
                perdedor = entrena2
                self.perdedores.append(perdedor)
                ganadores.append(ganador)
            print(f'*{duelo[0][0]} usando al programon {duelo[0][1]},\
 se enfrenta a {duelo[1][0]} usando al programon {duelo[1][1]}')
            print(f'    {ganador} ha ganado la batalla')
        self.ronda_actual += 1
        return ganadores

    



