lista_entrenas = [['Kaylee Robinson', ['Reshiram'], 87, ['raro+', 'ziuela']], ['Ricardo Walters', ['GyaradosMega Gyarados', 'Chimchar', 'Leavanny', 'Talonflame'], 60, ['curaTotal']], ['Juan Vaughn', 
['KeldeoOrdinary Forme', 'Luvdisc', 'Kyogre', 'Grovyle'], 90, ['restos', 'aranja']], ['Lori Wheeler', ['Heatmor', 'Poliwrath', 'Prinplup'], 9, ['impetu+']], ['Kellie Stokes', ['Huntail', 'Emboar'], 97, ['antiparalizante', 'despertar', 'antihielo']], ['Michael Hanna', ['Simipour'], 26, ['mente']], ['James Small', ['Virizion', 'RotomHeat Rotom'], 3, ['aguante', 'meloc', 'impetu']], ['Charles Cooley', ['Magmar', 'Starmie', 'Poliwag'], 30, ['musculo', 'rimoya']], ['Cassandra Taylor', ['Dewgong'], 58, ['antiquemar']], ['Mary Powell', ['Kabutops'], 25, ['zanama']], ['Thomas Stokes', ['Tentacool', 'Frogadier'], 69, ['revivir']], ['Jeffrey Miller', ['Palpitoad'], 83, ['perasi', 'intelecto', 'zidra', 'ango']], ['Kelli Morgan', 
['Cacnea', 'Dewott', 'Simisage'], 31, ['atania', 'intelecto+']], ['Dillon Velez', ['Blastoise', 'Gogoat'], 19, ['ispero']], ['Amy Solomon', ['Bulbasaur', 'Swadloon'], 82, ['pocion', 
'antidoto']], ['Suzanne Davies', ['Torchic', 'Sharpedo', 'BlazikenMega Blaziken'], 79, ['limonada']]]

todos_entrenas = ['Kaylee Robinson', 'Ricardo Walters', 'Juan Vaughn', 'Lori Wheeler', 'Kellie Stokes', 'Michael Hanna', 'James Small', 'Charles Cooley', 'Cassandra Taylor', 'Mary Powell', 'Thomas Stokes', 'Jeffrey Miller', 'Kelli Morgan', 'Dillon Velez', 'Amy Solomon', 'Suzanne Davies']

instanciar = LigaProgramon(lista_entrenas, 7, todos_entrenas)



entrenas_insta = instanciar.crear_entrenadores()
dic_entres_progras_insta = {}
for entrenador in entrenas_insta:
    entrena = entrenas_insta[entrenador]
    programones_insta = entrena.crear_programon()
    dic_entres_progras_insta[entrena.nombre] = {}
    for programon in programones_insta:
        dic_entres_progras_insta[entrena.nombre][programon] = programones_insta[programon]

#primera ronda
ganadore = instanciar.simular_ronda(dic_entres_progras_insta)
perdedores1 = instanciar.perdedores

#segunda ronda
dict2 = dic_entres_progras_insta.copy()
for perdedor in instanciar.perdedores:
    del dict2[perdedor]
holi = instanciar.simular_ronda(dict2)

#tercera ronda
dict3 = dic_entres_progras_insta.copy()
for perdedor in instanciar.perdedores:
    del dict3[perdedor]
hi = instanciar.simular_ronda(dict3)

#cuarta ronda
dict4 = dic_entres_progras_insta.copy()
for perdedor in instanciar.perdedores:
    del dict4[perdedor]
jello = instanciar.simular_ronda(dict4)


elif ronda == 2:
    perdedores1 = instanciar.perdedores
    dict2 = dic.copy()
    for perdedor in perdedores1:
        del dict2[perdedor]
    stop = instanciar.simular_ronda(dict2)
    if stop == 'perdio':
        para = True
    else:
        para = False
elif ronda == 3:
    dict3 = dic.copy()
    for perdedor in instanciar.perdedores:
        del dict3[perdedor]
    stop = instanciar.simular_ronda(dict3)
    if stop == 'perdio':
        para = True
    else:
        para = False
elif ronda == 4:
    dict4 = dic.copy()
    for perdedor in instanciar.perdedores:
        del dict4[perdedor]
    stop = instanciar.simular_ronda(dict4)
    if stop == 'perdio':
        para = True
    else:
        para = False
