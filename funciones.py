
from funciones_funcionamiento import checkeador
import sys
from LigaProgramon import LigaProgramon
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
        
        todos_entrenas = []
        for entrenador in lista_entrenadores:
            todos_entrenas.append(entrenador[0])

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

        if int(numero_menu) <16:
            lista_atributos_entrenador = lista_entrenadores[int(seleccion)]
            instanciar = LigaProgramon(lista_entrenadores,int(seleccion), todos_entrenas)
            entrenas_insta = instanciar.crear_entrenadores()
            dic_entres_progras_insta = {}
            for entrenador in entrenas_insta:
                entrena = entrenas_insta[entrenador]
                programones_insta = entrena.crear_programon()
                dic_entres_progras_insta[entrena.nombre] = {}
                for programon in programones_insta:
                    dic_entres_progras_insta[entrena.nombre][programon] = programones_insta[programon]

            stop = menu_entrenador(instanciar, dic_entres_progras_insta)
        else: 
            sys.exit()
    #hacer un ciclo que entregue atributos de cada uno de los entrenadores
    # Crear entrenadores

def menu_entrenador(instanciar, dic):
    para = 0
    while para != True:
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
           
        elif seleccion == '2':
            ronda = instanciar.ronda_actual
            print(f'ronda {ronda}')
            stop = accion_simular_ronda(instanciar,dic)
            if stop == 'perdio':
                para = True 
            else:
                if ronda == 4:
                    print('GANASTEEEEEEEEEEEE!')
                para = False
           
        elif seleccion == '3':
            print("crea obj")
      
        elif seleccion == '5':
            print('utilizar')
      
        elif seleccion == '6':
            print('estado entrena')
           
        elif seleccion == '7':
            return False
        elif seleccion == '0':
            sys.exit()
    return False
         

def accion_simular_ronda(instanciar, dic):
    ronda = instanciar.ronda_actual
    if ronda ==  1:
        ganadores = instanciar.simular_ronda(dic)
        if instanciar.nombre_entrenador in ganadores:
            return 'gano'
        else:
            print('Perdiste!')
            print()
            return 'perdio'
    if ronda == 2:
        dict2 = dic.copy()
        for perdedor in instanciar.perdedores:
            del dict2[perdedor]
        ganadores = instanciar.simular_ronda(dict2))
        if instanciar.nombre_entrenador in ganadores:
            return 'gano'
        else:
            print('Perdiste!')
            print()
            return 'perdio'
    if ronda == 3:
        dict3 = dic.copy()
        for perdedor in instanciar.perdedores:
            del dict3[perdedor]
        ganadores = instanciar.simular_ronda(dict3)
        if instanciar.nombre_entrenador in ganadores:
            return 'gano'
        else:
            print('Perdiste!')
            print()
            return 'perdio'
    if ronda == 4:
        dict4 = dic.copy()
        for perdedor in instanciar.perdedores:
            del dict4[perdedor]
        ganadores = instanciar.simular_ronda(dict4)
        if instanciar.nombre_entrenador in ganadores:
            return 'gano'
        else:
            print('Perdiste!')
            print()
            return 'perdio'
        
    
menu_inicio()


    


    






