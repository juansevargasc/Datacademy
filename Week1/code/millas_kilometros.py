def millas_a_kilometros(millas):
    '''
    1 mi = 1.609344 Km
    '''
    return millas * 1.609344

def kilometros_a_millas(kilometros):
    '''
    1 km = 0.62137119 mi
    '''
    return kilometros * 0.621371


if __name__ == '__main__':
    print('CONVERSOR MILLAS - KILÓMETROS')
    print("¿Qué deseas convertir?\n1. Millas a kilómetros\n2. Kilómetros a millas")

    opcion = int( input('\nIntroduce tu opción: ') )
    
    if opcion == 1:
        num = float( input('Introduce el número en Millas (mi):  ' ) )
        kilom = millas_a_kilometros(num)
        print(f'{kilom} km')
    elif opcion == 2:
        num = float( input('Introduce el número en Kilómetros (km):  ' ) )
        mill = kilometros_a_millas(num)
        print(f'{mill} mi')
    else:
        print('Opción incorrecta')

    
