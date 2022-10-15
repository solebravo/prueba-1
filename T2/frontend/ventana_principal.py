from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
import parametros as p
import os
import sys

class VentanaPrincipal(QWidget):
    senal_abrir_noche= pyqtSignal(str)
    senal_abrir_abuela = pyqtSignal(str)
    senal_enviar_usuario = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setGeometry(60, 60, 650, 450)
        self.setWindowTitle('VentanaInicio')
        self.crear_elementos()

    def crear_elementos(self):
        #fondo
        self.label_imagen = QLabel(self)
        self.label_imagen.setGeometry(0, 0, 650, 450)
        pixeles = QPixmap(p.RUTA_FONDO)
        self.label_imagen.setPixmap(pixeles)
        self.label_imagen.setScaledContents(True)

        #botones escenario
        self.abuela = QPushButton(self)
        self.abuela.setGeometry(38, 150, 250, 145)
        self.abuela.setIcon(QIcon(p.RUTA_AMBIENTE_ABUELA))
        self.abuela.setIconSize(QSize(330,145))

        self.noche = QPushButton(self)
        self.noche.setGeometry(366, 150, 250, 145)
        self.noche.setIcon(QIcon(p.RUTA_AMBIENTE_NOCHE))
        self.noche.setIconSize(QSize(330,145))

        self.abuela.clicked.connect(self.abrir_abuela)
        self.noche.clicked.connect(self.abrir_noche)

    def abrir_abuela(self):
        self.senal_abrir_abuela.emit(p.RUTA_AMBIENTE_ABUELA)
        self.hide()

    def abrir_noche(self):
        self.senal_abrir_noche.emit(p.RUTA_AMBIENTE_NOCHE)
        self.hide()

    def mostrar_ventana(self, usuario):
        self.show()
       

