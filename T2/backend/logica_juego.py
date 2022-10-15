from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication
import parametros as p
from backend.elementos import Zombie, Tablero
from random import randint
from aparicion_zombies import intervalo_aparicion
from copy import deepcopy

class LogicaJuego(QObject):
    senal_datos_iniciales = pyqtSignal(str, str, str, str)
    senal_crear_zombie = pyqtSignal(bool)
    senal_mover_zombie = pyqtSignal()
    senal_actualizar_datos = pyqtSignal(str, str, str, str, str)
    senal_obtener_coordenadas = pyqtSignal()
    senal_planta_comprada = pyqtSignal(str,list, int, int)
    senal_disparar = pyqtSignal(int)
    senal_girasol = pyqtSignal(bool)
    senal_bala = pyqtSignal(bool)
    senal_mover_bala = pyqtSignal(int)
    senal_multiples_bala = pyqtSignal()
    senal_crear_multiples_zombies =pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        super().__init__()
        #cambiar rutas a variables
        self.zombie = Zombie()
        self.timer_posicion = QTimer()
        self.timer_mover = QTimer()
        self.timer_planta = QTimer()
        self.timer_disparo = QTimer()
        self.timer_mover_bala = QTimer()
        self.timer_multiples_balas = QTimer()
        #self.timer_multiples_balas = QTimer()
        self.timer_multiples_zombies = QTimer()
        self.flag = True
        
        
        self.tablero = Tablero()
        self.soles = p.SOLES_INICIALES
        self.puntaje = 0
        self.ronda = p.NIVEL_INICIAL
        self.z_destruidos = 0
        self.z_restantes = p.N_ZOMBIES * 2
        self.escenario_ele = 0
        self.intervalo_aparicion_zombies = 0

        self.x = 0
        self.y = 0
        self.x_casilla = 0
        self.y_casilla = 0
        self.tipo = 0
        self.bool_tienda = False
        self.contador = 0

        self.zombies_lane_1 = []
        self.posicion_lane_1 = []
        self.lista_zombies_posicio_1 =[]

        self.zombies_lane_2 = []
        self.posicion_lane_2 = []
        self.lista_zombies_posicio_2 =[]

        self.lista_rect_zombies_L1 = []
        self.lista_rect_zombies_L2 = []

        self.balas_existentes = []
        self.lista_pos_balas = []

        self.lista_rect_balas = []

        self.lista_planatas_creadas =[]
        self.zombies_instanciados_L2 = []
        self.zombies_instanciados_L1 = []
        
  
    #funciones zombies
    #caminar
    def timers(self):
        self.timer_posicion.setInterval(p.VELOCIDAD_ZOMBIE_APARICION)
        self.timer_posicion.timeout.connect(self.frames)

        self.timer_mover.setInterval(p.VELOCIDAD_ZOMBIE_APARICION)
        self.timer_mover.timeout.connect(self.mover_zombie)

        self.timer_planta.setInterval(p.INTERVALO_DISPARO)
        self.timer_planta.timeout.connect(self.cuadros)

        self.timer_multiples_zombies.setInterval(1)
        self.timer_multiples_zombies.timeout.connect(self.crear_zombies)
        self.bandera = 0

        self.signo = 0
        
    def starts(self):
        self.timer_posicion.start()
        self.timer_mover.start()
        self.timer_planta.start()
        self.timer_disparo.start()
        self.timer_mover_bala.start()
        self.timer_multiples_balas.start()
        #self.timer_multiples_balas.start()
        self.timer_multiples_zombies.start()
        self.timers()
        
        self.interseccion_zombie_bala()
        self.senal_datos_iniciales.emit(str(self.soles), str(self.ronda),
         str(self.puntaje), str(self.z_restantes))

    def actualizar_datos(self):
        self.senal_actualizar_datos.emit(str(self.soles), str(self.ronda),
         str(self.puntaje), str(self.z_destruidos), str(self.z_restantes))

    def escenario(self, fondo):
        if fondo == 0:
            self.escenario_ele = 'abuela'
        else:
            self.escenario_ele = 'noche'
        self.intervalo_zombie()
        self.actualizar_datos()
        
    def crear_zombies(self):
        indice = randint(0,1)
        elegido_1 = p.TIPOS_ZOMBIES[indice]
        indice_2 = randint(0,1)
        elegido_2 = p.TIPOS_ZOMBIES[indice_2]
        self.senal_crear_multiples_zombies.emit(elegido_1, elegido_2)
        self.timer_multiples_zombies.setInterval(self.intervalo_aparicion_zombies)
        pass

    def frames(self):
        
        if self.flag == True:
            self.senal_crear_zombie.emit(True)
            self.senal_girasol.emit(True)
            self.flag = False  
        else:
            self.senal_crear_zombie.emit(False)
            self.senal_girasol.emit(False)
            self.flag = True

    def cuadros(self):
        if self.bandera == 0:
            self.senal_disparar.emit(0)
            self.bandera += 1
            self.contador += 1
        elif self.bandera == 1:
            self.senal_disparar.emit(1)
            self.bandera += 1
            self.contador +=1
        elif self.bandera == 2:
            self.senal_disparar.emit(2)
            self.bandera = 0
            self.contador += 1
        if self.contador == 2:
           
            self.timer_mover_bala.setInterval(p.INTERVALO_DISPARO)
            self.timer_mover_bala.timeout.connect(self.mover_bala)
            self.timer_disparo.setInterval(p.INTERVALO_DISPARO2)
            self.timer_disparo.timeout.connect(self.cuadros_disparo)
            self.timer_multiples_balas.setInterval(p.INTERVALO_DISPARO2)
            self.timer_multiples_balas.timeout.connect(self.crear_multiples_balas)

    def cuadros_disparo(self):
        #self.senal_bala.emit(0)
        if self.signo == 0:
            self.senal_bala.emit(0)
            self.signo += 1
        elif self.signo == 1:
            self.senal_bala.emit(1)
            self.signo += 1
        elif self.signo == 2:
            self.senal_bala.emit(2)
            self.signo = 0

    def mover_zombie(self):
        
        self.senal_mover_zombie.emit()

    def intervalo_zombie(self):
        if self.escenario_ele == 'abuela':
            ponderador = p.PONDERADOR_DIURNO
        elif self.escenario_ele == 'noche':
            ponderador = p.PONDERADOR_NOCTURNO
        inter = intervalo_aparicion(self.ronda, ponderador)*10000
        self.intervalo_aparicion_zombies = int(inter)


    def zombies_creados_lane_1(self, lista):
        self.zombies_lane_1 = lista
        if len(self.zombies_lane_1) == 7:
            self.timer_multiples_zombies.stop()
        self.lista_rect_zombies_L1.append([])
        self.zombies_instanciados_L1.append(self.zombie)

    def puestos_lane_1(self, lista):
        self.posicion_lane_1 = lista
        self.zombies_con_posicion()

    def zombies_creados_lane_2(self, lista):
        self.zombies_lane_2 = lista
        if len(self.zombies_lane_2) == 7:
            self.timer_multiples_zombies.stop()
        self.lista_rect_zombies_L2.append([])
        self.zombies_instanciados_L2.append(Zombie())

    def puestos_lane_2(self, lista):
        self.posicion_lane_2 = lista
        self.zombies_con_posicion()
        
        
    def zombies_con_posicion(self):
        for i in range(len(self.zombies_lane_1) - 1):
            if self.posicion_lane_1 != []:
                self.zombies_lane_1[i][2] = self.posicion_lane_1[i]
                rect_zombie = [self.zombies_lane_1[i][0] ,QRect(self.posicion_lane_1[i], 227, 45, 72)]

                self.lista_rect_zombies_L1[i] = rect_zombie
                
        for i in range(len(self.zombies_lane_2) - 1):
            if self.posicion_lane_2 != []:
                self.zombies_lane_2[i][2] = self.posicion_lane_2[i]
                rect_zombie = [self.zombies_lane_2[i][0] ,QRect(self.posicion_lane_2[i],115 , 45, 72 )]
                self.lista_rect_zombies_L2[i] = rect_zombie

        
        
    def balas_creadas(self, lista1, lista2):
        self.balas_existentes = lista1
        self.lista_rect_balas = lista2
        
    def posiciones_balas(self, lista):
        self.lista_pos_balas = lista
        for i in range(len(self.lista_rect_balas)):
            for j in range(len(self.lista_rect_balas[i])):
                rect = QRect(self.lista_pos_balas[i][j][1], self.lista_pos_balas[i][j][2], 20, 20)
                self.lista_rect_balas[i][j][1] = rect
        self.interseccion_zombie_bala()
        
        
    def interseccion_zombie_bala(self):
        
        for i in range(len(self.lista_rect_zombies_L1)):
            while self.zombies_instanciados_L1[i].vida > 0:
                for j in range(len(self.lista_rect_balas)):
                    for k in range(len(self.lista_rect_balas[j])):
                        print('en k',self.zombies_instanciados_L1[i])
                        if self.lista_rect_zombies_L1[i] !=[] and self.zombies_instanciados_L1[i] != 'nada':

                            boole = self.lista_rect_zombies_L1[i][1].intersects(self.lista_rect_balas[j][k][1])
                            if boole == True:
                                self.zombies_instanciados_L1[i].vida -= p.DANO_PROYECTIL
                                print(self.zombies_instanciados_L1[i].vida, self.zombies_instanciados_L1[i] )
                                if self.zombies_instanciados_L1[i].vida == 0:
                                    print('vida es 0')
                                    self.zombies_instanciados_L1[i] = 'nada'
                                    print(self.zombies_instanciados_L1[i])

                            
        
        for i in range(len(self.lista_rect_zombies_L2)):
            
            for j in range(len(self.lista_rect_balas)):
                for k in range(len(self.lista_rect_balas[j])):
                    if self.lista_rect_zombies_L2[i] !=[]:
                        boole = self.lista_rect_zombies_L2[i][1].intersects(self.lista_rect_balas[j][k][1])
                        if boole == True:
                            self.zombies_instanciados_L2[i].vida -= p.DANO_PROYECTIL
                            print(self.zombies_instanciados_L2[i].vida)
                            pass
                            

    
        
        

        
    def mover_bala(self):
        self.senal_mover_bala.emit('True')
        self.timer_mover_bala.setInterval(500)

    def crear_multiples_balas(self):
        self.senal_multiples_bala.emit()
    #tienda
    def coor_posi(self, x_, y_):
        self.x = x_
        self.y= y_
        self.validacion()
        
    def tienda(self, tipo):
        if tipo == 'girasol':
            if self.soles >= p.COSTO_GIRASOL:
                self.tipo = tipo
                self.bool_tienda = True
                return True
        elif tipo == 'clasica':
            if self.soles >= p.COSTO_LANZAGUISANTE:
                self.tipo = tipo
                self.bool_tienda = True
        elif tipo == 'azul':
            if self.soles >= p.COSTO_LANZAGUISANTE_HIELO:
                self.tipo = tipo
                self.bool_tienda = True
        elif tipo == 'papa':
            if self.soles >= p.COSTO_PAPA:
                self.tipo = tipo
                self.bool_tienda = True

    def validacion(self):
        #print(self.x, self.y)
        #print(self.tipo)
        dic_frames_tipos = p.DIC_FRAMES_PLANTAS
        if self.bool_tienda == True:
            if self.tablero.casillas(self.x) != 'afuera':
                if self.tablero.lanes(self.y) != 'afuera':
                    self.x_casilla = self.tablero.casillas(self.x)
                    #print('x', self.x)
                    self.y_casilla = self.tablero.lanes(self.y)
                    #print('x_casilla', self.x_casilla)
                    self.senal_planta_comprada.emit(self.tipo, dic_frames_tipos[self.tipo], 
                    self.x_casilla, self.y_casilla)
                    self.soles -= p.DIC_COSTOS[self.tipo]
                    self.actualizar_datos()

            else:
                print('fuera de pasto')
        else:
            print('demasiado pobre')
        



    
        
        
    

    