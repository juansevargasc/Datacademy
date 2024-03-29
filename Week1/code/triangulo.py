import math

def calculate_area( h, b ):
    return (h * b) / 2

def triangle_class(h, b):
    '''
    Sí es triángulo equilátero, h = sqrt(3) / 2 * b.
    Si es triángulo isósceles rectángulo h == b. En otros casos no funcionaría exactamente, haría falta saber más información.
    '''
    if h == ( (math.sqrt(3) / 2) * b ):
        return 'Equilátero'
    if h == b:
        return 'Isósceles'
    else:
        return 'Escaleno'


if __name__ == '__main__':
    base = int( input('Introduce la base ') )
    altura = int( input('Introduce la altura ') )

    area = calculate_area(base, altura)
    print(f'Area: {area}')

    clasificacion = triangle_class(base, altura)
    print(f'Clasificación: {clasificacion}')
    