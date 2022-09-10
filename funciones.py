from funciones_funcionamiento import checkeador
import sys
#MENUS
## Funciones necesarias Menu

def menu_inicio():
    with open('entrenadores.csv', 'r') as entrenas:
        contenido = entrenas.read()
        contenidos = contenido.split('\n')
        contenidos.pop(17)

        leng = len(contenidos) - 1
        lista_entrenas = []
        for value in contenidos:
            lista_entrenas.append(value.split(","))

        for value in range(0, 17):
                lista_entrenas[value ][1] = lista_entrenas[value ][1].split(';')
                lista_entrenas[value ][3] = lista_entrenas[value ][3].split(';')
        
        header = ['nombre', ['programones'], 'energia', ['objetos']]
        lista_entrenadores = [i for i in lista_entrenas if i != header]
        for value in range(0, 16):
                lista_entrenadores[value ][2] = int(lista_entrenadores[value ][2])
        
    print(lista_entrenadores)
    stop = 0
    while stop != True:
        print('Para comenzar debes ingresar el numero '
        'que corresponda al entrenador que desees utilizar')
        print()
        print('*MENU DE INICIO*')
        for numero in range(0, 16):
            print(f"[{numero}] {lista_entrenadores[numero][0]}: {lista_entrenadores[numero][1]} ")
        print('[16] Salir')

        numero_menu = input()
        while checkeador(17, numero_menu) != True:
            print('El caracter que haz ingresado no corresponde'
            ' ha alguna accion conocida, porfavor ingresa '
            'otro numero')
            numero_menu = input()
        seleccion = numero_menu
        #####OJO######
        stop = True
        #####OJO######
    if int(numero_menu) <16:
        lista_atributos_entrenador = lista_entrenadores[int(seleccion)]
        print(lista_atributos_entrenador)
    else: 
        sys.exit()
    #hacer un ciclo que entregue atributos de cada uno de los entrenadores
    # Crear entrenadores



lista_atributos_entrenador = ['Kaylee Robinson', ['Reshiram', 'gato'], '87', ['raro+', 'ziuela']]

def menu_entrenador(lista_atributos_entrenador):
    print()
    print('*MENU ENTRENADOR*')
    print('[1] Entrenamiento"RECUERDAD AGREGAR QUE SOLO SUCEDE SI ENERGIA ES SUFI"')
    print('[2] Simular ronda')
    print('[3] Resumen campeonato')
    print('[4] Crear objetos')
    print('[5] Utilizar objeto')
    print('[6] Estado entrenador')
    print('[7] Volver')
    print('[0] Salir')
    
    numero_menu = input()
    while checkeador(8, numero_menu) != True:
            print('El caracter que haz ingresado no corresponde'
            ' ha alguna accion conocida, porfavor ingresa '
            'otro numero')
            numero_menu = input()
    seleccion = numero_menu
    if seleccion == '1':
        print('aqui va funcion entrenamiento')
    
menu_inicio()


    


    



    


    






