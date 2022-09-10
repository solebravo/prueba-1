def checkeador(numero, numero_menu):
    numero_menu = str(numero_menu)
    numeros = []
    for i in range(0,numero):
        numeros.append(str(i))

    if numero_menu.isdigit() == True:
        opciones = numeros
        revisar = numero_menu in opciones
        if revisar == True:
            return True
    else:
        return False

def lector_programones():
    with open('programones.csv', 'r') as entrenas:
        contenido = entrenas.read()
        contenidos = contenido.split('\n')
        contenidos.pop(0)
        contenidos.pop(len(contenidos) - 1)
        leng = len(contenidos) - 1
        lista_programones = []
        for value in contenidos:
            lista_programones.append(value.split(","))
        return lista_programones

def diccionario_programones():
    lista_programones = lector_programones()
    nombres = []
    atributos = []
    for lista in lista_programones:
        nombres.append(lista[0])
        lista.pop(0)
        atributos.append(lista)
    dicc = zip(nombres, atributos)
    diccionario_programones = dict(dicc)
    return diccionario_programones

def diccionario(lista_completa):
    nombres = []
    atributos = []
    for lista in lista_completa:
        nombres.append(lista[0])
        #lista.pop(0)
        atributos.append(lista[1])
    dicc = zip(nombres, atributos)
    diccionario= dict(dicc)
    return diccionario

def lector_objetos():
    with open('objetos.csv', 'r') as objetos:
        contenido = objetos.read()
        contenidos = contenido.split('\n')
        contenidos.pop(0)
        contenidos.pop(len(contenidos) - 1)

        lista_programones = []
        for value in contenidos:
            lista_programones.append(value.split(","))
        return lista_programones



def diccionario_tipo_objeto(tipo):
    dic = diccionario(lector_objetos())
    objetos = {}
    for par in dic:
        if tipo == str(dic[par]):
            objetos[par] = dic[par]
    return objetos

