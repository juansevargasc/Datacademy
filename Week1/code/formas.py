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

def run():
    # Menu
    pass

if __name__ == '__main__':
    run()
