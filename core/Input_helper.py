def pedir_datos(estructura):

    opciones = {}
    for atribute in estructura.__annotations__.keys():
        user_input = input(f'Digite el {atribute}: ')
        opciones[atribute] = user_input
    return opciones



    
