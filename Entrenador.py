from Programon import Programon, ProgramonAgua, ProgramonFuego, ProgramonPlanta
from Objetos import Baya, Pocion, Caramelo
from funciones_funcionamiento import diccionario_programones, diccionario_tipo_objeto
from random import choice, randint
#############################################################################################################
#cuando lo pases a liga recuerda poner self
#def crear_programon(programones):
        #dic = diccionario_programones()
        #progras_instanciados = {}
        #cuando este dentro de Liga cambiar a self.programones
        #for programon in programones:
            #tipo = dic[programon][0]
            #if tipo == 'planta':
             #   progras_instanciados[programon] = ProgramonPlanta(dic[programon],programon)
            #elif tipo == 'fuego':
             #   progras_instanciados[programon] = ProgramonFuego(dic[programon],programon)   
            #else:
             #   progras_instanciados[programon] = ProgramonAgua(dic[programon],programon)

        #return progras_instanciados


#entren =  ['Ricardo Walters', ['GyaradosMega Gyarados', 'Chimchar', 'Leavanny', 'Talonflame'], 60, ['curaTotal']]
#programones = entren[1]


#print(Chimchar.experiencia)


#el diccionario se ve asi:
#{'GyaradosMega Gyarados': <Programon.ProgramonPlanta object at 0x0000022CB7A872E0>, 'Chimchar': <Programon.ProgramonPlanta object at 0x0000022CB7A871F0>, 'Leavanny': <Programon.ProgramonPlanta object at 0x0000022CB7A84550>, 'Talonflame': <Programon.ProgramonPlanta object at 0x0000022CB7A846D0>}
###########################################################################################################


class Entrenador():
    def __init__(self, atributos_entrenador):
        self.nombre = atributos_entrenador[0]
        self.programones = atributos_entrenador[1]
        self.energia = atributos_entrenador[2]
        self.objetos = atributos_entrenador[3]

    def crear_programon(self):
        dic = diccionario_programones()
        progras_instanciados = {}
        #cuando este dentro de Liga cambiar a self.programones
        for programon in self.programones:
            tipo = dic[programon][0]
            if tipo == 'planta':
                progras_instanciados[programon] = ProgramonPlanta(dic[programon],programon)
            elif tipo == 'fuego':
                progras_instanciados[programon] = ProgramonFuego(dic[programon],programon)   
            else:
                progras_instanciados[programon] = ProgramonAgua(dic[programon],programon)

        return progras_instanciados

    def estado_entrenador(self, programon_creado):
        print('*ESTADO ENTRENADOR*')
        print(f'NOMBRE: {self.nombre}')
        print(f'ENERGIA: {self.energia}')
        print('OBJETOS:', *self.objetos)
        print(f'PROGRAMONES:')
        for progra in self.programones:
            print(f'    {progra}')
            programon = programon_creado
            print(f'        Tipo: ', programon[progra].tipo)
            print(f'        Nivel: ', programon[progra].nivel)
            print(f'        Vida: ',programon[progra].vida)
            
    def crear_objetos(self,seleccion):
        dic_bayas = diccionario_tipo_objeto('baya')
        dic_pocion = diccionario_tipo_objeto('pocion')
        dic_caramelo = diccionario_tipo_objeto('caramelo')
        if str(seleccion) == "1":
            nombre = choice(list(dic_bayas))
            baya = Baya(nombre,dic_bayas[nombre])
            baya.aplicar()
            costo = baya.costo
            balance = self.energia - costo

            if balance >= 0:
                prob = randint(0,baya.prob_exito)

                if baya.prob_exito == prob:
                    self.objetos.append(nombre)
                    self.energia -= costo
                    
        elif str(seleccion) == '2':
            nombre = choice(list(dic_pocion))
            pocion = Pocion(nombre,dic_pocion[nombre])
            pocion.aplicar()
            costo = pocion.costo
            balance = self.energia - costo
            if balance >= 0:
                prob = randint(0,pocion.prob_exito)
                if pocion.prob_exito == prob:
                    self.objetos.append(nombre)
                    self.energia -= costo
        elif str(seleccion) == '3':
            nombre = choice(list(dic_caramelo))
            caramelo = Caramelo(nombre,dic_caramelo[nombre])
            caramelo.aplicar()
            costo = caramelo.costo
            balance = self.energia - costo
            if balance >= 0:
                prob = randint(0,caramelo.prob_exito)
                if caramelo.prob_exito == prob:
                    self.objetos.append(nombre)
                    self.energia -= costo

           
            



        

        
        





######################################################################################################
entrenas = [['Kaylee Robinson', ['Reshiram'], 87, ['raro+', 'ziuela']], ['Ricardo Walters', ['GyaradosMega Gyarados', 'Chimchar', 'Leavanny', 'Talonflame'], 60, ['curaTotal']], ['Juan Vaughn', ['KeldeoOrdinary Forme', 'Luvdisc', 'Kyogre', 'Grovyle'], 90, ['restos', 'aranja']], ['Lori Wheeler', ['Heatmor', 'Poliwrath', 'Prinplup'], 9, ['impetu+']], ['Kellie Stokes', ['Huntail', 'Emboar'], 97, ['antiparalizante', 'despertar', 'antihielo']], ['Michael Hanna', ['Simipour'], 26, ['mente']], ['James Small', ['Virizion', 'RotomHeat Rotom'], 3, ['aguante', 'meloc', 'impetu']], ['Charles Cooley', ['Magmar', 'Starmie', 'Poliwag'], 30, ['musculo', 'rimoya']], ['Cassandra Taylor', ['Dewgong'], 58, ['antiquemar']], ['Mary Powell', ['Kabutops'], 25, ['zanama']], ['Thomas Stokes', ['Tentacool', 'Frogadier'], 69, ['revivir']], ['Jeffrey Miller', ['Palpitoad'], 83, ['perasi', 'intelecto', 'zidra', 'ango']], ['Kelli Morgan', ['Cacnea', 'Dewott', 'Simisage'], 31, 
['atania', 'intelecto+']], ['Dillon Velez', ['Blastoise', 'Gogoat'], 19, ['ispero']], ['Amy Solomon', ['Bulbasaur', 'Swadloon'], 82, ['pocion', 'antidoto']], 
['Suzanne Davies', ['Torchic', 'Sharpedo', 'BlazikenMega Blaziken'], 79, ['limonada']]]

entren =  ['Ricardo Walters', ['GyaradosMega Gyarados', 'Chimchar', 'Leavanny', 'Talonflame'], 60, ['curaTotal']]

dict = {'Chimchar': ['fuego', '62', '43', '144', '86', '28'], 'Cacnea': ['planta', '40', '171', '158', '122', '49'], 'Torchic': ['fuego', '28', '65', '65', '60', '124'], 'BlazikenMega Blaziken': ['fuego', '15', '120', '42', '132', '184'], 'Virizion': ['planta', '53', '32', '178', '36', '18'], 'Reshiram': ['fuego', '13', '24', '99', '43', '136'], 'Tentacool': ['agua', '3', '87', '130', '129', '87'], 'Starmie': ['agua', '66', '208', '106', '92', '124'], 'RotomHeat Rotom': ['fuego', '10', '187', '187', '71', '90'], 'Magmar': ['fuego', '38', '178', '20', '122', '165'], 'Bulbasaur': ['planta', '50', '252', '123', '115', '13'], 'Luvdisc': ['agua', '68', '214', '188', '97', '27'], 'Talonflame': ['fuego', '41', '25', '159', '173', '18'], 'Simipour': ['agua', '70', '120', '177', '87', '15'], 'Simisage': ['planta', '66', '220', '127', '126', '36'], 'Kyogre': ['agua', '12', '241', '7', '111', '162'], 'Palpitoad': ['agua', '71', '240', '8', '201', '96'], 'Sharpedo': ['agua', '44', '179', '135', '75', '159'], 'Frogadier': ['agua', '32', '176', '143', '65', '52'], 'Kabutops': ['agua', '60', '13', '80', '53', '20'], 'Heatmor': ['fuego', '13', '215', '108', '106', '187'], 'Gogoat': ['planta', '63', '155', '63', '113', '134'], 'Prinplup': ['agua', '63', '34', '100', '135', '130'], 'Leavanny': ['planta', '64', '117', '161', '61', '162'], 'KeldeoOrdinary Forme': ['agua', '46', '174', '85', '139', '172'], 'Huntail': ['agua', '15', '208', '93', '242', '20'], 'Poliwrath': ['agua', '67', '98', '28', '135', '67'], 'Emboar': ['fuego', '73', '59', '30', '240', '110'], 'GyaradosMega Gyarados': ['agua', '5', '59', '167', '13', '143'], 'Dewgong': ['agua', '12', '1', '58', '71', '121'], 'Grovyle': ['planta', '26', '232', '90', '238', '52'], 'Swadloon': ['planta', '2', '222', '19', '152', '134'], 'Blastoise': ['agua', '60', '31', '179', '99', '132'], 'Dewott': ['agua', '56', '40', '149', '223', '153'], 'Poliwag': ['agua', '2', '208', '145', '169', '40']}
duelo = (('Thomas Stokes', 'Tentacool'), ('Ricardo Walters', 'Chimchar'))
progra1 = 'Chimchar'
atris1 = ['fuego', '62', '43', '144', '86', '28']



#entrenador = Entrenador(entren)
#programon_instanciado = entrenador.crear_programon()
#print(programon_instanciado)
#estado = entrenador.estado_entrenador(programon_instanciado)
#Chimchar = programon_instanciado['Chimchar']
#print(Chimchar.luchar(duelo, dict))


#clase = Entrenador(entren)
#progras_entrenador= clase.crear_programon()
#print(progras_entrenador)
#Chimchar = progras_entrenador['Chimchar'].vida
#print(Chimchar)

print()