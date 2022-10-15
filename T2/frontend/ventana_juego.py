from re import I
from PyQt5.QtCore import pyqtSignal, QSize, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QIcon, QMouseEvent
import parametros as p
import os
import sys
from copy import deepcopy

class VentanaJuego(QWidget):
    senal_enviar_usuario = pyqtSignal(str)
    senal_iniciar = pyqtSignal(str)

    senal_comprar = pyqtSignal(str)
    senal_posicion_compra = pyqtSignal(int,int)
    senal_fondo = pyqtSignal(int)

    senal_zombies_lane_1 = pyqtSignal(list)
    senal_puesto_lane_1 = pyqtSignal(list)
    senal_zombies_lane_2 = pyqtSignal(list)
    senal_puesto_lane_2 = pyqtSignal(list)

    senal_balas = pyqtSignal(list, list)
    senal_posiciones_balas = pyqtSignal(list)
    senal_lista_creacion_plantas = pyqtSignal(list)
    def __init__(self,ruta_fondo):
        super().__init__()
        self.setGeometry(0, 0, 1000, 600)
        self.setWindowTitle('VentanaJuego')
        self.ruta = p.RUTA_AMBIENTE_ABUELA
        self.click_x = 0
        self.click_y = 0
        
        
        self.cant_plantas = 0
        self.lista_plantadas = []
        self.lista_tipo_plant = []
        self.movedor = 4
        self.cuenta = 0
        self.num = 0
        self.zombies_lane_1 = []
        self.puesto_lane_1 = []
        self.zombies_lane_2 = []
        self.puesto_lane_2 = []

        self.lista_balas_backend= []
        
        self.posicion_balas_l1 =[]
        self.posicion_balas_l2 =[]
        self.lista_listosa = []

        #self.timer_desplaza = QTimer(self)
    def ruta_fondo(self, fondo):
        self.ruta = fondo
        self.crear_elementos()
        self.show()
        
        if fondo == 'sprites\Fondos\jardinAbuela.png':
            self.senal_fondo.emit(0)
        else:
            self.senal_fondo.emit(1)

        
    def crear_elementos(self):
        #fondo
        self.label_color_fondo = QLabel(self)
        self.label_color_fondo.setGeometry( 0, 0, 1000, 600)
        self.label_color_fondo.setStyleSheet("background-color: rgb(46,218,40)")

        #fondo ambiente
        self.label_ambiente_abuela = QLabel(self)
        self.label_ambiente_abuela.setGeometry(160, 0, 1100, 440)
        pixeles = QPixmap(self.ruta)
        self.label_ambiente_abuela.setPixmap(pixeles)
        self.label_ambiente_abuela.setScaledContents(True)

        #color barra
        self.color_barra = QLabel(self)
        self.color_barra.setGeometry(160,440,900,170)
        self.color_barra.setStyleSheet("background-color: rgb(32,144,28)")

        #botones
        #posicionar
        self.boton_posicionar = QPushButton(self)
        self.boton_posicionar.setGeometry(31, 10, 90, 25 )
        self.boton_posicionar.setStyleSheet("background-color: rgb(121,255,43)" )
        self.boton_posicionar.setText('posicionar')
        #girasol
        self.tienda_girasol = QPushButton(self)
        self.tienda_girasol.setGeometry(31, 46, 90, 90)
        self.tienda_girasol.setStyleSheet("background-color: rgb(121,255,43)")
        self.tienda_girasol.setIcon(QIcon('girasol_1.png'))
        self.tienda_girasol.setIconSize(QSize(80,80))
        self.label_precio_girasol = QLabel(self)
        self.label_precio_girasol.setGeometry(65, 143, 81, 30)
        self.label_precio_girasol.setText('50')
        self.label_precio_girasol.setStyleSheet( "font-size: 18pt;")
        #planta clasica
        self.tienda_clasica = QPushButton(self)
        self.tienda_clasica.setGeometry(31, 180, 90, 90)
        self.tienda_clasica.setStyleSheet("background-color: rgb(121,255,43)")
        self.tienda_clasica.setIcon(QIcon('lanzaguisantes_1.png'))
        self.tienda_clasica.setIconSize(QSize(80,80))
        self.label_precio_clasica = QLabel(self)
        self.label_precio_clasica.setGeometry(65, 277, 81, 30)
        self.label_precio_clasica.setText('50')
        self.label_precio_clasica.setStyleSheet( "font-size: 18pt;")
        #planta azul
        self.tienda_azul = QPushButton(self)
        self.tienda_azul.setGeometry(31, 314, 90, 90)
        self.tienda_azul.setStyleSheet("background-color: rgb(121,255,43)")
        self.tienda_azul.setIcon(QIcon('lanzaguisantesHielo_1.png'))
        self.tienda_azul.setIconSize(QSize(80,80))
        self.label_precio_azul = QLabel(self)
        self.label_precio_azul.setGeometry(60, 412, 81, 30)
        self.label_precio_azul.setText('100')
        self.label_precio_azul.setStyleSheet( "font-size: 18pt;")
        #planta papa
        self.tienda_papa = QPushButton(self)
        self.tienda_papa.setGeometry(31, 458, 90, 90)
        self.tienda_papa.setStyleSheet("background-color: rgb(121,255,43)")
        self.tienda_papa.setIcon(QIcon('papa_1.png'))
        self.tienda_papa.setIconSize(QSize(80,80))
        self.label_precio_papa = QLabel(self)
        self.label_precio_papa.setGeometry(65, 555, 81, 30)
        self.label_precio_papa.setText('75')
        self.label_precio_papa.setStyleSheet( "font-size: 18pt;")

        #labels barra
        #soles
        self.label_soles = QLabel(self)
        self.label_soles.setGeometry(188, 455, 100, 50)
        self.label_soles.setStyleSheet("background-color: rgb(0,100,0);"
         "qproperty-alignment: AlignCenter;" "font-size: 18pt;")
        self.label_soles.setText('Soles')
        self.soles_cant = QLabel(self)
        self.soles_cant.setGeometry(188, 520, 100, 50)
        self.soles_cant.setStyleSheet( "qproperty-alignment: AlignCenter;"
         "font-size: 18pt;")
        #nivel
        self.label_nivel = QLabel(self)
        self.label_nivel.setGeometry(318, 455, 100, 50)
        self.label_nivel.setStyleSheet("background-color: rgb(0,100,0);" 
        "qproperty-alignment: AlignCenter;" "font-size: 18pt;")
        self.label_nivel.setText('Nivel')
        self.nivel = QLabel(self)
        self.nivel.setGeometry(318, 520, 100, 50)
        self.nivel.setStyleSheet( "qproperty-alignment: AlignCenter;" 
        "font-size: 18pt;")
        #puntaje
        self.label_puntaje = QLabel(self)
        self.label_puntaje.setGeometry(448, 455, 100, 50)
        self.label_puntaje.setStyleSheet("background-color: rgb(0,100,0);" 
        "qproperty-alignment: AlignCenter;" "font-size: 18pt;")
        self.label_puntaje.setText('Puntaje')
        self.puntaje_actual = QLabel(self)
        self.puntaje_actual.setGeometry(448, 520, 100, 50)
        self.puntaje_actual.setStyleSheet( "qproperty-alignment: AlignCenter;" "font-size: 18pt;")
        #zombies destruidos
        self.label_zd = QLabel(self)
        self.label_zd.setGeometry(578, 455, 200, 65)
        self.label_zd.setStyleSheet("background-color: rgb(0,100,0);" 
        "qproperty-alignment: AlignCenter;" "font-size: 15pt;")
        self.label_zd.setText('Zombies destruidos')
        self.zombies_destruidos = QLabel(self)
        self.zombies_destruidos.setGeometry(778, 455, 65, 65)
        self.zombies_destruidos.setStyleSheet( "qproperty-alignment: AlignCenter;" "font-size: 18pt;")
        #zombies restantes
        self.label_zr = QLabel(self)
        self.label_zr.setGeometry(578, 530, 200, 65)
        self.label_zr.setStyleSheet("background-color: rgb(0,100,0);" 
        "qproperty-alignment: AlignCenter;" "font-size: 15pt;")
        self.label_zr.setText('Zombies restantes')
        self.zombies_restantes = QLabel(self)
        self.zombies_restantes.setGeometry(778, 530, 65, 65)
        self.zombies_restantes.setStyleSheet( "qproperty-alignment: AlignCenter;" "font-size: 18pt;")

        #botones
        #iniciar
        self.boton_iniciar = QPushButton('Iniciar', self)
        self.boton_iniciar.setGeometry(860, 455, 120, 30)
        self.boton_iniciar.setStyleSheet("background-color: rgb(0,100,0);" "font-size: 12pt;")
        #avanzar
        self.boton_avanzar = QPushButton('Avanzar', self)
        self.boton_avanzar.setGeometry(860, 490, 120, 30)
        self.boton_avanzar.setStyleSheet("background-color: rgb(0,100,0);" "font-size: 12pt;")
        #pausa
        self.boton_pausa = QPushButton('Pausar', self)
        self.boton_pausa.setGeometry(860, 525, 120, 30)
        self.boton_pausa.setStyleSheet("background-color: rgb(0,100,0);" "font-size: 12pt;")
        #Salir
        self.boton_salir = QPushButton('Salir', self)
        self.boton_salir.setGeometry(860, 560, 120, 30)
        self.boton_salir.setStyleSheet("background-color: rgb(0,100,0);" "font-size: 12pt;")

        


        self.boton_iniciar.clicked.connect(self.iniciar)
        self.boton_salir.clicked.connect(self.salir)
       
        self.boton_posicionar.clicked.connect(self.pos_click)
        self.tienda_girasol.clicked.connect(self.comprar_girasol)
        self.tienda_clasica.clicked.connect(self.comprar_clasica)
        self.tienda_azul.clicked.connect(self.comprar_azul)
        self.tienda_papa.clicked.connect(self.comprar_papa)

    def datos_iniciales(self, soles, nivel, puntaje, restantes):
        self.soles_cant.setText(soles)
        self.nivel.setText(nivel)
        self.puntaje_actual.setText(puntaje)
        self.zombies_destruidos.setText('0')
        self.zombies_restantes.setText(restantes)
    
    def actualizar_datos(self, soles, nivel, puntaje, destruidos, restantes):
        self.soles_cant.setText(soles)
        self.nivel.setText(nivel)
        self.puntaje_actual.setText(puntaje)
        self.zombies_destruidos.setText(destruidos)
        self.zombies_restantes.setText(restantes)

    def crear_zombies(self,elegido_1, elegido_2):
        zombie = QLabel(self)
        zombie.setGeometry(883, 227, 45, 72)
        zombie.setScaledContents(True)
        lista = [zombie, p.DIC_ZOMBIES[elegido_1], 883, 227, elegido_1]
        self.puesto_lane_1.append(883)
        self.zombies_lane_1.append(lista)

        zombie = QLabel(self)
        zombie.setGeometry(883, 155, 45, 72)
        zombie.setScaledContents(True)
        lista = [zombie, p.DIC_ZOMBIES[elegido_2], 883, 155, elegido_2]
        self.puesto_lane_2.append(883)
        self.zombies_lane_2.append(lista)


        self.senal_zombies_lane_1.emit(self.zombies_lane_1)
        self.senal_zombies_lane_2.emit(self.zombies_lane_2)
        

    def crear_plantas(self):
        self.label_planta = QLabel(self)
        self.label_planta.setGeometry(878, 225, 60, 80)

    def frames(self, flag):
        for i in range(len(self.zombies_lane_1)):
            if self.zombies_lane_1[i][0] != 'nada':
                if flag == True:
                    pixeles = QPixmap(self.zombies_lane_1[i][1][0])
                    self.zombies_lane_1[i][0].setPixmap(pixeles)
                    self.zombies_lane_1[i][0].setScaledContents(True)
                    self.zombies_lane_1[i][0].show()

                    pixeles = QPixmap(self.zombies_lane_2[i][1][0])
                    self.zombies_lane_2[i][0].setPixmap(pixeles)
                    self.zombies_lane_2[i][0].setScaledContents(True)
                    self.zombies_lane_2[i][0].show()
                    #self.flag = False
                else:
                    pixeles = QPixmap(self.zombies_lane_1[i][1][1])
                    self.zombies_lane_1[i][0].setPixmap(pixeles)
                    self.zombies_lane_1[i][0].setScaledContents(True)
                    self.zombies_lane_1[i][0].show()

                    pixeles = QPixmap(self.zombies_lane_2[i][1][1])
                    self.zombies_lane_2[i][0].setPixmap(pixeles)
                    self.zombies_lane_2[i][0].setScaledContents(True)
                    self.zombies_lane_2[i][0].show()
            #self.flag = True

    def cuadros_girasol(self, flag):
        for i in range(len(self.lista_plantadas)):
            if self.lista_plantadas[i][2] == 'girasol':
                if flag == True:
                    pixeles = QPixmap(self.lista_plantadas[i][1][0])
                    self.lista_plantadas[i][0].setPixmap(pixeles)
                    self.lista_plantadas[i][0].setScaledContents(True)
                    self.lista_plantadas[i][0].show()
                        #self.flag = False
                else:
                    pixeles = QPixmap(self.lista_plantadas[i][1][1])
                    self.lista_plantadas[i][0].setPixmap(pixeles)
                    self.lista_plantadas[i][0].setScaledContents(True)
                    self.lista_plantadas[i][0].show()
                    
    def cuadros_no_girasol(self, bandera):
        for i in range(len(self.lista_plantadas)):
            if self.lista_plantadas[i][2] != 'girasol':
                if bandera == 0:
                    pixeles = QPixmap(self.lista_plantadas[i][1][0])
                    self.lista_plantadas[i][0].setPixmap(pixeles)
                    self.lista_plantadas[i][0].setScaledContents(True)
                    self.lista_plantadas[i][0].show()
                    
                if bandera == 1:
                    pixeles = QPixmap(self.lista_plantadas[i][1][1])
                    self.lista_plantadas[i][0].setPixmap(pixeles)
                    self.lista_plantadas[i][0].setScaledContents(True)
                    self.lista_plantadas[i][0].show()
                if bandera == 2:
                    pixeles = QPixmap(self.lista_plantadas[i][1][2])
                    self.lista_plantadas[i][0].setPixmap(pixeles)
                    self.lista_plantadas[i][0].setScaledContents(True)
                    self.lista_plantadas[i][0].show()
                    
    def guisantes(self, signo):
        for i in range(len(self.lista_plantadas)):
            if self.lista_plantadas[i][2] == 'azul' or self.lista_plantadas[i][2] == 'clasica':
                for j in range(len(self.lista_plantadas[i][5])):
                    frames = p.DIC_BALA[self.lista_plantadas[i][2]]
                    self.lista_plantadas[i][5][j][0].setGeometry(self.lista_plantadas[i][3] + 30,
                     self.lista_plantadas[i][4] + 10, 20, 20)
                    pixeles = QPixmap(frames[0])
                    self.lista_plantadas[i][5][j][0].setPixmap(pixeles)
                    self.lista_plantadas[i][5][j][0].setScaledContents(True)
                    self.lista_plantadas[i][5][j][0].show()
                self.lista_balas_backend[i].append([self.lista_plantadas[i][5][j][0],
                self.lista_plantadas[i][3], self.lista_plantadas[i][4] ] )
                self.lista_listosa[i].append([self.lista_plantadas[i][5][j][0], 'Qrect', 
                self.lista_plantadas[i][2]])
                    
        self.senal_balas.emit(self.lista_balas_backend, self.lista_listosa)
                          
            
    def plantar(self, tipo, frames, x, y):
        if tipo == 'clasica' or tipo == 'azul':
            
            tupla = [QLabel(self), frames, tipo, x, y, []]
            self.lista_plantadas.append(tupla)
            self.lista_plantadas[self.cant_plantas][0].setGeometry(x, y, 58, 73)
            pixeles = QPixmap(frames[0])
            self.lista_plantadas[self.cant_plantas][0].setPixmap(pixeles)
            self.lista_plantadas[self.cant_plantas][0].setScaledContents(True)
            self.lista_plantadas[self.cant_plantas][0].show()
            self.cant_plantas += 1
            print(y)
            
            self.lista_balas_backend.append([])
            self.lista_listosa.append([])
            
        else:
            tupla = [QLabel(self), frames, tipo,x, y, []]
            self.lista_plantadas.append(tupla)
            self.lista_plantadas[self.cant_plantas][0].setGeometry(x, y, 58, 73)
            pixeles = QPixmap(frames[0])
            self.lista_plantadas[self.cant_plantas][0].setPixmap(pixeles)
            self.lista_plantadas[self.cant_plantas][0].setScaledContents(True)
            self.lista_plantadas[self.cant_plantas][0].show()
            self.cant_plantas += 1

        
        
##############
    def anadir_bala(self):
        for i in range(len(self.lista_plantadas)):
            
            if self.lista_plantadas[i][2] == 'azul' or self.lista_plantadas[i][2] == 'clasica':

                lista = [QLabel(self), 3, self.lista_plantadas[i][4]]
                self.lista_plantadas[i][5].append(lista)
        for i in range(len(self.lista_plantadas)):
            if self.lista_plantadas[i][5] != []:
                if self.lista_plantadas[i][4] == 153:
                    lista_1 = [self.lista_plantadas[i][0], self.lista_plantadas[i][2], 
                    self.lista_plantadas[i][3], self.lista_plantadas[i][4]]

                else:
                    
                    lista_1 = [self.lista_plantadas[i][0], self.lista_plantadas[i][2], 
                    self.lista_plantadas[i][3], self.lista_plantadas[i][4]]

    def mover_zombie(self):
        for i in range(len(self.zombies_lane_1)):
            if self.zombies_lane_1[i][1][0] == p.RUTA_Z_CLASIC_W_1: 
                #for j in len(self.zombies_lane_1[i]):
                if self.puesto_lane_1[i] > 357:
                    self.puesto_lane_1[i] -= p.VELOCIDAD_ZOMBIE
                    self.zombies_lane_1[i][0].move(self.puesto_lane_1[i] , 227)
                else:
                    if self.zombies_lane_1[i][0] != 'nada':
                        print('hide')
                        
                        self.zombies_lane_1[i][0].hide()
                        self.zombies_lane_1[i][0] = 'nada'
                    
            elif self.zombies_lane_1[i][1][0] == p.RUTA_Z_OTRO_1:
                if self.puesto_lane_1[i] > 357:
                    self.puesto_lane_1[i] -= p.VELOCIDAD_ZOMBIE_X_1_5
                    self.zombies_lane_1[i][0].move(self.puesto_lane_1[i] , 227)
                else:
                    if self.zombies_lane_1[i][0] != 'nada':
                        print('hide')
                        self.zombies_lane_1[i][0].hide()
                        self.zombies_lane_1[i][0] = 'nada'
            self.senal_puesto_lane_1.emit(self.puesto_lane_1)

        for i in range(len(self.zombies_lane_2)):
            if self.zombies_lane_2[i][1][0] == p.RUTA_Z_CLASIC_W_1: 
                #for j in len(self.zombies_lane_1[i]):
                if self.puesto_lane_2[i] > 357:
                    self.puesto_lane_2[i] -= p.VELOCIDAD_ZOMBIE
                    self.zombies_lane_2[i][0].move(self.puesto_lane_2[i] , 155)
                else:
                    if self.zombies_lane_2[i][0] != 'nada':
                        print('hide')
                        self.zombies_lane_2[i][0].hide()
                        self.zombies_lane_2[i][0] = 'nada'
            elif self.zombies_lane_2[i][1][0] == p.RUTA_Z_OTRO_1:
                if self.puesto_lane_2[i] > 357:
                    self.puesto_lane_2[i] -= p.VELOCIDAD_ZOMBIE_X_1_5
                    self.zombies_lane_2[i][0].move(self.puesto_lane_2[i] , 155)
                else:
                    if self.zombies_lane_2[i][0] != 'nada':
                        print('hide')
                        
                        self.zombies_lane_2[i][0].hide()
                        self.zombies_lane_2[i][0] = 'nada'
            self.senal_puesto_lane_2.emit(self.puesto_lane_2)
        

    def mover_bala(self):
        for i in range(len(self.lista_plantadas)):
            if self.lista_plantadas[i][2] == 'azul' or self.lista_plantadas[i][2] == 'clasica':
                for j in range(len(self.lista_plantadas[i][5])):
                    x = self.lista_plantadas[i][3]
                    movedor = self.lista_plantadas[i][5][j][1]
                    x += movedor
                    self.lista_plantadas[i][5][j][1] += 30
                    self.lista_plantadas[i][5][j][0].move(x + 30, self.lista_plantadas[i][4] + 10)
                    self.lista_balas_backend[i][j][1] = x + 30
        self.senal_posiciones_balas.emit(self.lista_balas_backend)
        
        
        
        

         

    #TIENDA
    def comprar_girasol(self):
        self.senal_comprar.emit('girasol')

    def comprar_clasica(self):
        self.senal_comprar.emit('clasica')

    def comprar_azul(self):
        self.senal_comprar.emit('azul')

    def comprar_papa(self):
        self.senal_comprar.emit('papa')

    def mousePressEvent(self, QMouseEvent):
        self.click_y = QMouseEvent.y()
        self.click_x = QMouseEvent.x()
        print(self.click_x, self.click_y)

    def pos_click(self):
        self.senal_posicion_compra.emit(self.click_x, self.click_y)
        
    

    def iniciar(self):
        self.senal_iniciar.emit('yes')
        # for i in range(len(self.lista_plantadas)):
        #     self.lista_plantadas[i].hide()
        
    def salir(self):
        self.close()
        





