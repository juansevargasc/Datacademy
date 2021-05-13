import random

def ppt(seleccion_jugador1, seleccion_jugador2):
    '''
    Partida de 3. Gana el jugador que gane 2 de tres encuentros.
    '''
    # Definiciones
    piedra_papel_tijera = ['Piedra', 'Papel', 'Tijera']
    puntos = [0, 0]

    for i in range(3):
        if i > 0:
            # Selección aleatoria para cada jugador, después de la primera partida.
            seleccion_jugador1 = random.choice(piedra_papel_tijera)
            seleccion_jugador2 = random.choice(piedra_papel_tijera)
        
        # Información
        print(f'Partida {i + 1}')
        print(f'Jugador 1: {seleccion_jugador1} - Jugador 2: {seleccion_jugador2}')


        # Jugar y acumular puntos
        puntos_partida = jugar(seleccion_jugador1, seleccion_jugador2)
        zipped_lists = zip(puntos_partida, puntos) 
        puntos = sum = [x + y for (x, y) in zipped_lists] # Create a list with the sum of each pair

        # Puntos
        print(f'PUNTOS {puntos[0]} -  {puntos[1]}\n')
    
    # Selección del ganador
    if puntos[0] == 2 or puntos[0] == 3:
        return "¡El ganador es el jugador 1!" 
    elif puntos[1] == 2 or puntos[1] == 3:
        return "¡El ganador es el jugador 2!"
    else:
        return "No hay ganador :("

def jugar(seleccion_jugador1, seleccion_jugador2):
    count1, count2 = 0, 0
    if seleccion_jugador1 == 'Piedra':
            if seleccion_jugador2 == 'Tijera':
                count1 += 1
            elif seleccion_jugador2 == 'Papel':
                count2 += 1
            else:
                pass
                
    elif seleccion_jugador1 == 'Papel':
        if seleccion_jugador2 == 'Piedra':
            count1 += 1
        elif seleccion_jugador2 == 'Tijera':
            count2 += 1
        else:
            pass
    
    else:
        if seleccion_jugador2 == 'Papel':
            count1 += 1
        elif seleccion_jugador2 == 'Piedra':
            count2 += 1
        else:
            pass
    
    return [count1, count2]

if __name__ == '__main__':
    # Selección
    piedra_papel_tijera = ['Piedra', 'Papel', 'Tijera']

    # Selección aleatoria para cada jugador
    jugador1 = random.choice(piedra_papel_tijera)
    jugador2 = random.choice(piedra_papel_tijera)

    print( ppt(jugador1, jugador2) )