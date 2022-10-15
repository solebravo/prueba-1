from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p

class LogicaInicio(QObject):

    senal_respuesta_usuario = pyqtSignal(bool, set)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobacion_usuario(self, usuario):
        print('comproba')
        error_alnum = 0
        error_largo = 0
        if usuario.isalnum() == True:
            error_alnum = 0
        else:
            error_alnum = "alfanumerico"
       

        if len(usuario) < p.MIN_CARACTERES:
            error_largo = "corto"
        elif len(usuario) > p.MAX_CARACTERES:
            error_largo = "largo"

        sete = set()
        if error_alnum == 0 and error_largo == 0 :
            self.senal_respuesta_usuario.emit(True, sete)
            self.senal_abrir_juego.emit(usuario)
        elif error_alnum != 0 and error_largo == 0 :
            sete.add('alfanumerico')
            self.senal_respuesta_usuario.emit(False, sete)
        elif error_alnum == 0 and error_largo != 0 :
            if error_largo == 'corto':
                sete.add('corto')
                self.senal_respuesta_usuario.emit(False, sete)
            elif error_largo == 'largo':
                sete.add('largo')
                self.senal_respuesta_usuario.emit(False, sete)
        elif error_alnum != 0 and error_largo != 0 :
            sete.add('alfanumerico')
            if error_largo == 'corto':
                sete.add('corto')
                self.senal_respuesta_usuario.emit(False, sete)
            elif error_largo == 'largo':
                sete.add('largo')
                self.senal_respuesta_usuario.emit(False, sete)




        