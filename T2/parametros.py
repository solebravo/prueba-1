import os

# Los intervalos están en milisegundos
INTERVALO_DISPARO = 1000 
INTERVALO_DISPARO2 = 3000
INTERVALO_SOLES_GIRASOL = 20000
INTERVALO_TIEMPO_MORDIDA = 5000
# El daño y la vida tienen las mismas medidas
DANO_PROYECTIL = 10
DANO_MORDIDA = 5
VIDA_PLANTA = 100
VIDA_ZOMBIE = 50
# Número de zombies por carril
N_ZOMBIES = 7
# Porcentaje de ralentización
RALENTIZAR_ZOMBIE = 0.25
# Soles iniciales por ronda
SOLES_INICIALES = 250
# Número de soles generados por planta
CANTIDAD_SOLES = 2
# Número de soles agregados a la cuenta por recolección
SOLES_POR_RECOLECCION = 50
# Número de soles agregados a la cuenta por Cheatcode
SOLES_EXTRA = 25
# Ponderadores de escenarios
PONDERADOR_NOCTURNO = 0.8
PONDERADOR_DIURNO = 0.9
# La velocidad del zombie en milisegundos
VELOCIDAD_ZOMBIE_APARICION = 750
VELOCIDAD_ZOMBIE = 10
VELOCIDAD_ZOMBIE_X_1_5 = 15
# Puntaje por eliminar zombie
PUNTAJE_ZOMBIE_DIURNO = 50
PUNTAJE_ZOMBIE_NOCTURNO = 100
# Costo por avanzar de ronda
COSTO_AVANZAR = 500
# Costo tiendasF
COSTO_LANZAGUISANTE = 50
COSTO_LANZAGUISANTE_HIELO = 100
COSTO_GIRASOL = 50
COSTO_PAPA = 75
# Caracteres de nombre usuario
MIN_CARACTERES = 3
MAX_CARACTERES = 15

VELOCIDAD_DISPARO = 500


RUTA_FONDO = os.path.join('sprites', 'Fondos', 'fondoMenu.png' )
RUTA_AMBIENTE_ABUELA = os.path.join('sprites', 'Fondos', 'jardinAbuela.png' )
RUTA_AMBIENTE_NOCHE = os.path.join('sprites', 'Fondos', 'salidaNocturna.png' )
RUTA_Z_CLASIC_W_1 = os.path.join('sprites','Zombies', 'Caminando','zombieHernanRunner_1.png' )
RUTA_Z_CLASIC_W_2 = os.path.join('sprites','Zombies', 'Caminando','zombieHernanRunner_2.png' )
RUTA_Z_OTRO_1 =  os.path.join('sprites','Zombies', 'Caminando','zombieNicoWalker_1.png' )
RUTA_Z_OTRO_2 =  os.path.join('sprites','Zombies', 'Caminando','zombieNicoWalker_2.png' )


RUTA_GIRASOL_1 = os.path.join('sprites', 'Plantas', 'girasol_1.png')
RUTA_GIRASOL_2 = os.path.join('sprites', 'Plantas', 'girasol_2.png')
RUTA_CLASICA_1 = os.path.join('sprites', 'Plantas', 'lanzaguisantes_1.png')
RUTA_CLASICA_2 = os.path.join('sprites', 'Plantas', 'lanzaguisantes_2.png')
RUTA_CLASICA_3 = os.path.join('sprites', 'Plantas', 'lanzaguisantes_3.png')
RUTA_AZUL_1 = os.path.join('sprites', 'Plantas', 'lanzaguisantesHielo_1.png')
RUTA_AZUL_2 = os.path.join('sprites', 'Plantas', 'lanzaguisantesHielo_2.png')
RUTA_AZUL_3 = os.path.join('sprites', 'Plantas', 'lanzaguisantesHielo_3.png')
RUTA_PAPA_1 = os.path.join('sprites', 'Plantas', 'papa_1.png')
RUTA_PAPA_2 = os.path.join('sprites', 'Plantas', 'papa_2.png')
RUTA_PAPA_3 = os.path.join('sprites', 'Plantas', 'papa_3.png')

RUTA_GUISA_CLASIC_1 = os.path.join('sprites', 'Elementos de juego', 'guisante_1.png')
RUTA_GUISA_CLASIC_2 = os.path.join('sprites', 'Elementos de juego', 'guisante_2.png')
RUTA_GUISA_CLASIC_3 = os.path.join('sprites', 'Elementos de juego', 'guisante_3.png')
RUTA_GUISA_AZUL_1 = os.path.join('sprites', 'Elementos de juego', 'guisanteHielo_1.png')
RUTA_GUISA_AZUL_2 = os.path.join('sprites', 'Elementos de juego', 'guisanteHielo_2.png')
RUTA_GUISA_AZUL_3 = os.path.join('sprites', 'Elementos de juego', 'guisanteHielo_3.png')


POS_INICIAL_ZOMBIE_L2_X = 878
POS_ZOMBIE_L2_Y = 225

NIVEL_INICIAL = 1

X_COMIENZO = 359
X_FINAL =935
Y_ARRIBA = 153
Y_MEDIO = 226
Y_ABAJO = 299
TAMANO_CAS = 58

Y_LANE_1 = 227

DIC_FRAMES_PLANTAS = { 'girasol' : [RUTA_GIRASOL_1, RUTA_GIRASOL_2], 
'clasica':[RUTA_CLASICA_1, RUTA_CLASICA_2, RUTA_CLASICA_3],
'azul':[RUTA_AZUL_1,RUTA_AZUL_2,RUTA_AZUL_3],
'papa': [RUTA_PAPA_1, RUTA_PAPA_2, RUTA_PAPA_3] }
DIC_BALA = {'clasica':[RUTA_GUISA_CLASIC_1, RUTA_GUISA_CLASIC_2, RUTA_GUISA_CLASIC_3], 
'azul': [RUTA_GUISA_AZUL_1, RUTA_GUISA_AZUL_2, RUTA_GUISA_AZUL_3]}
DIC_COSTOS = {'girasol': COSTO_GIRASOL, 'clasica': COSTO_LANZAGUISANTE, 
'azul': COSTO_LANZAGUISANTE_HIELO, 'papa': COSTO_PAPA}
DIC_ZOMBIES = {'hernan':[RUTA_Z_CLASIC_W_1, RUTA_Z_CLASIC_W_2], 
'nico': [RUTA_Z_OTRO_1, RUTA_Z_OTRO_2]}

TIPOS_ZOMBIES = ['hernan', 'nico']
