from random import randint
from parametros import ENERGIA_ENTRENAMIENTO, MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA \
    , MAX_AUMENTO_ENTRENAMIENTO, MIN_AUMENTO_ENTRENAMIENTO
from abc import ABC, abstractmethod



class Programon(ABC):

    def __init__(self, programon_elegido_atris, programon_elegido):

        self.nombre = programon_elegido
        self.tipo = programon_elegido_atris[0]
        self.nivel = int(programon_elegido_atris[1])
        self.vida = int(programon_elegido_atris[2])
        self.ataque = int(programon_elegido_atris[3])
        self.defensa = int(programon_elegido_atris[4])
        self.velocidad = int(programon_elegido_atris[5])
        self.experiencia = 0


    @property
    def entrenamiento(self):
        return self.experiencia

    @entrenamiento.setter
    def entrenamiento(self, valor_experiencia):
        print(f'experiencia inicio: {self.experiencia}')
        numero = randint(MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA)
        self.experiencia += numero
        print(self.experiencia)
        niveles_subidos = 0
        if self.experiencia >= 100:
            self.nivel += 1
            niveles_subidos += 1
            suma = self.experiencia - 100
            self.experiencia = suma
        if niveles_subidos > 0:
            self.vida += randint(MIN_AUMENTO_ENTRENAMIENTO,MAX_AUMENTO_ENTRENAMIENTO)
            self.ataque += randint(MIN_AUMENTO_ENTRENAMIENTO,MAX_AUMENTO_ENTRENAMIENTO)
            self.defensa += randint(MIN_AUMENTO_ENTRENAMIENTO,MAX_AUMENTO_ENTRENAMIENTO)
            self.velocidad += randint(MIN_AUMENTO_ENTRENAMIENTO,MAX_AUMENTO_ENTRENAMIENTO)
        if self.nivel >= 100:
            self.experiencia == 0
            if self.nivel > 100:
                self.nivel = 100
    
    @abstractmethod
    def luchar(self):
        pass
 
class ProgramonPlanta(Programon):

    def __init__(self, programon_elegido_atris, programon_elegido):
        super().__init__(programon_elegido_atris, programon_elegido)
            

    def luchar(self, duelo, dicc_atributos):
        self.duelo = duelo
        self.dicc_atributos = dicc_atributos
        atributos_update = [self.tipo, self.nivel, self.ataque , self.defensa, self.velocidad]
        self.dicc_atributos[self.nombre] = atributos_update
        #buscar por llave los tipos de ambos
        for nombre in duelo:
            if nombre[1] != self.nombre:
                progra_contrincante = nombre[1]
        tipo_programon = self.tipo
        atris_contrincante = self.dicc_atributos[progra_contrincante]
        tipo_contrincante = atris_contrincante[0]
        if tipo_contrincante == 'fuego':
            ventaja = -1
        elif tipo_contrincante == 'agua':
            ventaja = 1
        elif tipo_contrincante == 'planta':
            ventaja = 0
        puntaje_victoria = max(0,self.vida * 0.2 + self.nivel * 0.3 + self.ataque * 0.15 \
            + self.defensa * 0.15 + self.velocidad * 0.2 + ventaja * 40 )
        return puntaje_victoria

class ProgramonFuego(Programon):

    def __init__(self, programon_elegido_atris, programon_elegido):
        super().__init__(programon_elegido_atris, programon_elegido)
           

    def luchar(self, duelo, dicc_atributos):
        self.duelo = duelo
        self.dicc_atributos = dicc_atributos 
        atributos_update = [self.tipo, self.nivel, self.ataque , self.defensa, self.velocidad]
        self.dicc_atributos[self.nombre] = atributos_update
        #buscar por llave los tipos de ambos
        for nombre in duelo:
            if nombre[1] != self.nombre:
                progra_contrincante = nombre[1]
        tipo_programon = self.tipo
        atris_contrincante = self.dicc_atributos[progra_contrincante]
        tipo_contrincante = atris_contrincante[0]
        if tipo_contrincante == 'fuego':
            ventaja = 0
        elif tipo_contrincante == 'agua':
            ventaja = -1
        elif tipo_contrincante == 'planta':
            ventaja = 1
        puntaje_victoria = max(0,self.vida * 0.2 + self.nivel * 0.3 + self.ataque * 0.15 \
            + self.defensa * 0.15 + self.velocidad * 0.2 + ventaja * 40 )
        return puntaje_victoria

class ProgramonAgua(Programon):

    def __init__(self, programon_elegido_atris, programon_elegido):
        super().__init__(programon_elegido_atris, programon_elegido)
          

    def luchar(self, duelo, dicc_atributos):
        self.duelo = duelo
        self.dicc_atributos = dicc_atributos  
        atributos_update = [self.tipo, self.nivel, self.ataque , self.defensa, self.velocidad]
        self.dicc_atributos[self.nombre] = atributos_update
        #buscar por llave los tipos de ambos
        for nombre in duelo:
            if nombre[1] != self.nombre:
                progra_contrincante = nombre[1]
        tipo_programon = self.tipo
        atris_contrincante = self.dicc_atributos[progra_contrincante]
        tipo_contrincante = atris_contrincante[0]
        if tipo_contrincante == 'fuego':
            ventaja = 1
        elif tipo_contrincante == 'agua':
            ventaja = 0
        elif tipo_contrincante == 'planta':
            ventaja = -1
        puntaje_victoria = max(0,self.vida * 0.2 + self.nivel * 0.3 + self.ataque * 0.15 \
            + self.defensa * 0.15 + self.velocidad * 0.2 + ventaja * 40 )
        return puntaje_victoria

#entrenas = [['Kaylee Robinson', ['Reshiram'], 87, ['raro+', 'ziuela']], ['Ricardo Walters', ['GyaradosMega Gyarados', 'Chimchar', 'Leavanny', 'Talonflame'], 60, ['curaTotal']], ['Juan Vaughn', ['KeldeoOrdinary Forme', 'Luvdisc', 'Kyogre', 'Grovyle'], 90, ['restos', 'aranja']], ['Lori Wheeler', ['Heatmor', 'Poliwrath', 'Prinplup'], 9, ['impetu+']], ['Kellie Stokes', ['Huntail', 'Emboar'], 97, ['antiparalizante', 'despertar', 'antihielo']], ['Michael Hanna', ['Simipour'], 26, ['mente']], ['James Small', ['Virizion', 'RotomHeat Rotom'], 3, ['aguante', 'meloc', 'impetu']], ['Charles Cooley', ['Magmar', 'Starmie', 'Poliwag'], 30, ['musculo', 'rimoya']], ['Cassandra Taylor', ['Dewgong'], 58, ['antiquemar']], ['Mary Powell', ['Kabutops'], 25, ['zanama']], ['Thomas Stokes', ['Tentacool', 'Frogadier'], 69, ['revivir']], ['Jeffrey Miller', ['Palpitoad'], 83, ['perasi', 'intelecto', 'zidra', 'ango']], ['Kelli Morgan', ['Cacnea', 'Dewott', 'Simisage'], 31, 
#['atania', 'intelecto+']], ['Dillon Velez', ['Blastoise', 'Gogoat'], 19, ['ispero']], ['Amy Solomon', ['Bulbasaur', 'Swadloon'], 82, ['pocion', 'antidoto']], 
#['Suzanne Davies', ['Torchic', 'Sharpedo', 'BlazikenMega Blaziken'], 79, ['limonada']]]

#entren =  ['Ricardo Walters', ['GyaradosMega Gyarados', 'Chimchar', 'Leavanny', 'Talonflame'], 60, ['curaTotal']]

#dict = {'Chimchar': ['fuego', '62', '43', '144', '86', '28'], 'Cacnea': ['planta', '40', '171', '158', '122', '49'], 'Torchic': ['fuego', '28', '65', '65', '60', '124'], 'BlazikenMega Blaziken': ['fuego', '15', '120', '42', '132', '184'], 'Virizion': ['planta', '53', '32', '178', '36', '18'], 'Reshiram': ['fuego', '13', '24', '99', '43', '136'], 'Tentacool': ['agua', '3', '87', '130', '129', '87'], 'Starmie': ['agua', '66', '208', '106', '92', '124'], 'RotomHeat Rotom': ['fuego', '10', '187', '187', '71', '90'], 'Magmar': ['fuego', '38', '178', '20', '122', '165'], 'Bulbasaur': ['planta', '50', '252', '123', '115', '13'], 'Luvdisc': ['agua', '68', '214', '188', '97', '27'], 'Talonflame': ['fuego', '41', '25', '159', '173', '18'], 'Simipour': ['agua', '70', '120', '177', '87', '15'], 'Simisage': ['planta', '66', '220', '127', '126', '36'], 'Kyogre': ['agua', '12', '241', '7', '111', '162'], 'Palpitoad': ['agua', '71', '240', '8', '201', '96'], 'Sharpedo': ['agua', '44', '179', '135', '75', '159'], 'Frogadier': ['agua', '32', '176', '143', '65', '52'], 'Kabutops': ['agua', '60', '13', '80', '53', '20'], 'Heatmor': ['fuego', '13', '215', '108', '106', '187'], 'Gogoat': ['planta', '63', '155', '63', '113', '134'], 'Prinplup': ['agua', '63', '34', '100', '135', '130'], 'Leavanny': ['planta', '64', '117', '161', '61', '162'], 'KeldeoOrdinary Forme': ['agua', '46', '174', '85', '139', '172'], 'Huntail': ['agua', '15', '208', '93', '242', '20'], 'Poliwrath': ['agua', '67', '98', '28', '135', '67'], 'Emboar': ['fuego', '73', '59', '30', '240', '110'], 'GyaradosMega Gyarados': ['agua', '5', '59', '167', '13', '143'], 'Dewgong': ['agua', '12', '1', '58', '71', '121'], 'Grovyle': ['planta', '26', '232', '90', '238', '52'], 'Swadloon': ['planta', '2', '222', '19', '152', '134'], 'Blastoise': ['agua', '60', '31', '179', '99', '132'], 'Dewott': ['agua', '56', '40', '149', '223', '153'], 'Poliwag': ['agua', '2', '208', '145', '169', '40']}
#duelo = (('Thomas Stokes', 'Tentacool'), ('Ricardo Walters', 'Chimchar'))
#progra1 = 'Chimchar'
#atris1 = ['fuego', '62', '43', '144', '86', '28']
#agua = ProgramonAgua(atris1, progra1)
#planta = ProgramonPlanta(atris1, progra1)
#fuego = ProgramonFuego(atris1, progra1)
#print(agua.luchar(duelo, dict))
