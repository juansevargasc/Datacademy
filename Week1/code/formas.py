import math

def cylinder_volume(radius, height):
    '''
    Returns pi * radius^2 * height
    '''
    return (math.pi * (radius ** 2) ) * height

def cube_volume(edge_length):
    '''
    Returns edge_length^3
    '''
    return (edge_length ** 3)

def pyramid_volume(height, edge):
    '''
    Returns 1/3 * (height * edge)
    '''
    return 1/3 * (height * edge)

def sphere_volume(radius):
    '''
    Returns 4/3 * (pi * (radius^3) )
    '''
    return 4/3 * (math.pi * (radius ** 3) )

def cone_volume(radius, height):
    '''
    Returns 1/3 * (pi * (radius^2) * height)
    '''
    return 1/3 * (math.pi * (radius ** 2) * height)

def print_menu():
    print("1. Cilindro: Radio, Altura")
    print("2. Cubo: Lado")
    print("3. Pirámide: Altura, Lado")
    print("4. Esfera: Radio")
    print("5. Cone: Radio, Altura\n")

def run():
    # Menu
    print_menu()
    option = input('Elige qué quieres calcular y provee por favor los datos indicados: ')
    
    
    #Menu
    if option == '1':
        radio = int(input('Radio: '))
        altura = int(input('Altura: '))
        print(f'V = {cylinder_volume(radio, altura)}')
    if option == '2':
        lado = int(input('Lado: '))
        print(f'V = {cube_volume(lado)}')
    if option == '3':
        altura = int(input('Altura: '))
        lado = int(input('Lado: '))
        print(f'V = {pyramid_volume(altura, lado)}')
    if option == '4':
        radio = int(input('Radio: '))
        print(f'V = {sphere_volume(radio)} ')
    if option == '5':
        radio = int(input('Radio: '))
        altura = int(input('Altura: '))
        print(f'V = {cone_volume(radio, altura)}')
    else:
        print('Opción No Válida')

if __name__ == '__main__':
    run()
