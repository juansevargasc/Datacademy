def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname":"Facundo", "lastname":"García"}

    # Lista de diccionarios
    super_list = [
        {"firstname":"Facundo", "lastname":"García"},
        {"firstname":"Facundo", "lastname":"García"},
        {"firstname":"Facundo", "lastname":"García"},
        {"firstname":"Facundo", "lastname":"García"},
        {"firstname":"Facundo", "lastname":"García"}

    ]

    # Diccionario de listas
    super_dict = {
        "natural_nums" : [1, "Hello", True, 4.5], 
        "integer_nums" : [1, "Hello", True, 4.5],
        "floating_nums" : [1, "Hello", True, 4.5]
    }

    
    

if __name__ == '__main__':
    run()