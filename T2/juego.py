from PyQt5.QtWidgets import QApplication
import sys
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego
from frontend.ventana_principal import VentanaPrincipal
import parametros as p

class Juego(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.ventana_principal = VentanaPrincipal()
        

        self.ventana_inicio = VentanaInicio()
        self.ventana_inicio.show()
        self.logica_inicio = LogicaInicio()

        self.ventana_juego = VentanaJuego(p.RUTA_AMBIENTE_ABUELA)
        
        self.logica_juego = LogicaJuego()
        self.conecciones_juego()
        self.conecciones_inicio()
        self.conecciones_principal()

    def conecciones_inicio(self):
        self.ventana_inicio.senal_enviar_usuario.connect(self.logica_inicio.comprobacion_usuario)

        self.logica_inicio.senal_respuesta_usuario.connect(self.ventana_inicio.recibir_validacion)
        self.logica_inicio.senal_abrir_juego.connect(self.ventana_principal.mostrar_ventana)

    def conecciones_principal(self):
        self.ventana_principal.senal_abrir_abuela.connect(self.ventana_juego.ruta_fondo)
        self.ventana_principal.senal_abrir_noche.connect(self.ventana_juego.ruta_fondo)
    def conecciones_juego(self):
        
        self.ventana_juego.senal_iniciar.connect(self.logica_juego.starts)
        self.ventana_juego.senal_comprar.connect(self.logica_juego.tienda)
        self.ventana_juego.senal_posicion_compra.connect(self.logica_juego.coor_posi)

        self.ventana_juego.senal_zombies_lane_1.connect(self.logica_juego.zombies_creados_lane_1)
        self.ventana_juego.senal_puesto_lane_1.connect(self.logica_juego.puestos_lane_1)
        self.ventana_juego.senal_zombies_lane_2.connect(self.logica_juego.zombies_creados_lane_2)
        self.ventana_juego.senal_puesto_lane_2.connect(self.logica_juego.puestos_lane_2)
        
        self.ventana_juego.senal_balas.connect(self.logica_juego.balas_creadas)
        self.ventana_juego.senal_posiciones_balas.connect(self.logica_juego.posiciones_balas)
        #self.ventana_juego.senal_lista_creacion_plantas.connect(self.logica_juego.planta_creada)
        ###########
        self.ventana_juego.senal_fondo.connect(self.logica_juego.escenario)

        self.logica_juego.senal_crear_zombie.connect(self.ventana_juego.frames)
        self.logica_juego.senal_mover_zombie.connect(self.ventana_juego.mover_zombie)
        self.logica_juego.senal_crear_multiples_zombies.connect(self.ventana_juego.crear_zombies)

        self.logica_juego.senal_datos_iniciales.connect(self.ventana_juego.datos_iniciales)
       
        self.logica_juego.senal_actualizar_datos.connect(self.ventana_juego.actualizar_datos)
        self.logica_juego.senal_planta_comprada.connect(self.ventana_juego.plantar)
        self.logica_juego.senal_disparar.connect(self.ventana_juego.cuadros_no_girasol)
        
        self.logica_juego.senal_girasol.connect(self.ventana_juego.cuadros_girasol)
        
        self.logica_juego.senal_bala.connect(self.ventana_juego.guisantes)
        self.logica_juego.senal_mover_bala.connect(self.ventana_juego.mover_bala)
        self.logica_juego.senal_multiples_bala.connect(self.ventana_juego.anadir_bala)
        

if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)
    sys.__excepthook__ = hook

    juego = Juego(sys.argv)
    # juego.iniciar()
    sys.exit(juego.exec())