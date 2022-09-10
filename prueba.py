#n_jugadores = []
        #for i in range(len(self.entrenadores)):
            #n_jugadores.append(i)
        posible = programones_contrincantes.copy()
        jugador1 = []
        jugador2 = []
        while posible != []:
            elegido1 = choice(posible)
            jugador1.append(elegido1)
            idex = posible.index(elegido1)
            posible.pop(idex)
            print(posible)