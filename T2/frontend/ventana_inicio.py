from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
import parametros as p
import os
import sys

class VentanaInicio(QWidget):
    senal_enviar_usuario = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setGeometry(60, 60, 450, 450)
        self.setWindowTitle('VentanaInicio')
        self.crear_elementos()
        
    def crear_elementos(self):
        #fondo
        self.label_imagen = QLabel(self)
        self.label_imagen.setGeometry(0, 0, 450, 450)
        pixeles = QPixmap(p.RUTA_FONDO)
        self.label_imagen.setPixmap(pixeles)
        self.label_imagen.setScaledContents(True)
        #logo
        ruta_logo = os.path.join('sprites', 'Elementos de juego', 'logo.png')
        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap(ruta_logo))
        self.logo.setScaledContents(True)
        #ingreso usuario
        self.nombre_usuario = QLineEdit('', self)
        self.label_nombre_usuario = QLabel("Ingresa tu nombre de usuario", self)
        #boton jugar
        self.boton_jugar = QPushButton("Jugar", self)
        #boton ranking
        self.boton_ranking = QPushButton("Ranking", self)
        #boton salir
        self.boton_salir = QPushButton("Salir", self)

        #Layouts
        lay_vertical = QVBoxLayout()
        #lay_vertical.addWidget(self.label_imagen)
        lay_vertical.addWidget(self.logo)
        lay_vertical.addWidget(self.label_nombre_usuario)
        lay_vertical.addWidget(self.nombre_usuario)
        lay_vertical.addWidget(self.boton_jugar)
        lay_vertical.addWidget(self.boton_ranking)
        lay_vertical.addWidget(self.boton_salir)
        
        self.setLayout(lay_vertical)
        
        

        #botones
        self.boton_jugar.clicked.connect(self.enviar_usuario)
        self.boton_ranking.clicked.connect(self.ver_ranking)
        self.boton_salir.clicked.connect(self.salir)

    

        self.show()

    def enviar_usuario(self):
        self.senal_enviar_usuario.emit(self.nombre_usuario.text())

    def recibir_validacion(self, boole, sete):

        if boole == True:
            self.close()
        if 'alfanumerico' in sete:
            if 'largo' in sete:
                self.nombre_usuario.setText('')
                text = 'nombre de usuario tiene elementos no alfanumericos y mas de 15 caracteres'
                self.nombre_usuario.setPlaceholderText(text)
            elif 'corto' in sete:
                self.nombre_usuario.setText('')
                text = 'nombre de usuario tiene elementos no alfanumericos y menos de 3 caracteres'
                self.nombre_usuario.setPlaceholderText(text)
            else:
                self.nombre_usuario.setText('')
                text = 'nombre de usuario tiene elementos no alfanumericos'
                self.nombre_usuario.setPlaceholderText(text)
        elif 'largo' in sete:
            self.nombre_usuario.setText('')
            text = 'nombre de usuario tiene mas de 15 caracteres'
            self.nombre_usuario.setPlaceholderText(text)
        elif 'corto' in sete:
            self.nombre_usuario.setText('')
            text = 'nombre de usuario tiene menos de 3 caracteres'
            self.nombre_usuario.setPlaceholderText(text)

    def ver_ranking(self):
        pass

    def salir(self):
        self.close()














        



