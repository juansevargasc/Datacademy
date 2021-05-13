def calculate_area( h, b ):
    return (h * b) / 2

def triangle_class(h, b):
    return None


if __name__ == '__main__':
    base = int( input('Introduce la base ') )
    altura = int( input('Introduce la altura ') )

    area = calculate_area(base, altura)
    print(f'Area: {area}')
    
